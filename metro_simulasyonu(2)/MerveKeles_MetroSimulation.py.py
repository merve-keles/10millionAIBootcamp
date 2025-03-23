import heapq  # öncelik kuyruğu (heapq) kullanmak için gerekli modül

class MetroGraph:
    def __init__(self):
        self.graph = {}              #ist ve bağl saklayan sözlük
        self.transfer_stations = {}  #akt ist hatlara göre saklayan sözlük
        self.travel_time = 2         #iki ist arası süre
        self.transfer_time = 4       #akt yapma süresi
        self.base_fare = 25          #ilk biniş ücret
        self.transfer_fare = 5       #her aktarma için ek ücret

    def add_station(self, line, station, is_transfer=False):
        #eğer ist grafte yoksa, grafe ekle
        if station not in self.graph:
            self.graph[station] = []
        #eğer hat transfer ist sözlüğünde yoksa, ekle
        if line not in self.transfer_stations:
            self.transfer_stations[line] = []
        # eğer ist bir akt ist ise, ilgili hat listesine ekle
        if is_transfer:
            self.transfer_stations[line].append(station)

    def add_connection(self, station1, station2):
        #iki ist arasında çift yönlü bağlantı ekle
        self.graph[station1].append(station2)
        self.graph[station2].append(station1)

    def bfs_least_transfers(self, start, goal):
        #bfs için kuyruk: (mevcut ist, rota, aktarma sayısı)
        queue = [(start, [start], 0)]
        visited = set()         #ziyaret edilen ist sakla
        while queue:
            current, path, transfers = queue.pop(0)     #kuyruktan ilk elemanı al
            if current == goal:                         #eğer hedefe ulaşıldıysa
                return self._simplify_route(path), transfers  #rotayı ve aktarma sayısını döndür
            if current not in visited:                  #eğer ist daha önce ziyaret edilmemişse
                visited.add(current)                    #ist ziyaret edildi olarak işaretle
                for neighbor in self.graph[current]:    #komşu ist gez
                    #eğer ist bir akt ist ise
                    is_transfer = any(current in self.transfer_stations[line] for line in self.transfer_stations)
                    #kuyruğa yeni rotayı ve aktarma sayısını ekle
                    queue.append((neighbor, path + [neighbor], transfers + (1 if is_transfer else 0)))
        return None  #eğer rota bulunamazsa none döndür

    def a_star_fastest_route(self, start, goal):
        #a* için öncelik kuyruğu: (tahmini maliyet, mevcut ist, rota, gerçek maliyet)
        heap = [(0, start, [start], 0)]
        visited = {}         #ziyaret edilen istasyonları ve maliyetlerini sakla
        while heap:
            cost, current, path, real_cost = heapq.heappop(heap)    #kuyruktan en düşük maliyetli elemanı al
            if current == goal:              #eğer hedefe ulaşıldıysa
                return self._simplify_route(path), real_cost    #rotayı ve gerçek maliyeti döndür
            if current in visited and visited[current] <= real_cost:    #eğer daha önce ziyaret edildiyse ve maliyet daha düşükse
                continue        #bu istasyonu atla
            visited[current] = real_cost            #ist ziyaret edildi olarak işaretle ve maliyeti kaydet
            for neighbor in self.graph[current]:    #komşu ist gez
                #eğer ist bir akt ist ise
                is_transfer = any(current in self.transfer_stations[line] for line in self.transfer_stations)
                #yeni maliyeti hesapla (aktarma süresi veya seyahat süresi ekle)
                new_cost = real_cost + (self.transfer_time if is_transfer else self.travel_time)
                #kuyruğa yeni rotayı ve maliyeti ekle
                heapq.heappush(heap, (new_cost, neighbor, path + [neighbor], new_cost))
        return None      #eğer rota bulunamazsa none döndür

    def calculate_fare(self, path):
        #rotadaki akt sayısını hesapla
        transfers = sum(1 for i in range(1, len(path)) if any(path[i] in self.transfer_stations[line] for line in self.transfer_stations))
        #toplam ücr hesapla: ilk biniş + (aktarma sayısı * aktarma ücreti)
        return self.base_fare + (transfers * self.transfer_fare)

    def _simplify_route(self, path):
        #rotayı basitleştir: sadece bşlngç, akt ist ve bitiş ist göster
        simplified = [path[0]]          #bşlngç istasyonu ekle
        for i in range(1, len(path)):
            if any(path[i] in self.transfer_stations[line] for line in self.transfer_stations):  # eğer istasyon bir aktarma istasyonu ise
                simplified.append(path[i])      #rotaya ekle
        simplified.append(path[-1])             #bitiş ist ekle
        return simplified                       #basitleştirilmiş rotayı döndür

# metro ağı oluştur
metro = MetroGraph()

# hatlar ve istasyonlar
lines = {
    "M1": ["Kızılay", "Sıhhıye", "Ulus", "Atatürk Kültür Merkezi", "Akköprü", "İvedik", "Yenimahalle", "Demetevler", "Hastane", "Macunköy", "Ostim", "Batıkent"],
    "M2": ["Kızılay", "Necatibey", "Milli Kütüphane", "Söğütözü", "MTA", "ODTÜ", "Bilkent", "Tarım Bakanlığı-Danıştay", "Beytepe", "Ümitköy", "Çayyolu", "Koru"],
    "M3": ["Batıkent", "Batı Merkez", "Mesa", "Botanik", "İstanbul Yolu", "Eryaman 1-2", "Eryaman 5", "Devlet Mah.", "Harikalar Diyarı", "Fatih", "GOP", "OSB Törekent"],
    "M4": ["Kızılay", "Adliye", "Gar", "AKM", "ASKİ", "Dışkapı", "Meteoroloji", "Belediye", "Mecidiye", "Kuyubaşı", "Dutluk", "Gazino"],
    "Ankaray": ["Dikimevi", "Kurtuluş", "Kolej", "Kızılay", "Demirtepe", "Maltepe", "Anadolu", "Beşevler", "Bahçelievler", "Emek", "AŞTİ"],
    "Başkentray": ["Sincan", "Lale", "Elvankent", "Eryaman YHT", "Özgüneş", "Etimesgut", "Hava Durağı", "Behiçbey", "Marşandiz", "Gazi", "Gazi Mahallesi", "Hipodrom", "Ankara", "Sıhhıye", "Kurtuluş", "Cebeci", "Demirlibahçe", "Saimekadın", "Mamak", "Bağderesi", "Üreğil", "Köstence", "Kayaş"]
}

# aktarma istasyonları
transfer_stations = {
    "Kızılay": ["M1", "M2", "M4", "Ankaray"],
    "Sıhhıye": ["M1", "Başkentray"],
    "Yenimahalle": ["M1", "Yenimahalle-Şentepe Teleferik"],
    "Batıkent": ["M1", "M3"],
    "Söğütözü": ["M2", "Ankaray"],
    "Kurtuluş": ["Ankaray", "Başkentray"],
    "AŞTİ": ["Ankaray", "Başkentray"]
}

#hatlara ve ist göre metro ağını oluştur
for line, stations in lines.items():
    for i, station in enumerate(stations):
        is_transfer = station in transfer_stations      #eğer ist bir akt ist ise
        metro.add_station(line, station, is_transfer)   #istasyonu ekle
        if i > 0:  # eğer ilk istasyon değilse
            metro.add_connection(stations[i - 1], station)  # önceki istasyonla bağlantı kur

# test senaryoları
tests = [
    ("Batıkent", "Kızılay"),
    ("Eryaman 5", "Ümitköy"),
    ("Dikimevi", "Gazino"),
    ("Sincan", "Çayyolu")
]

# test senaryolarını çalıştır ve sonuçları yazdır
print("-" * 50 + "test senaryoları" + "-" * 50)
for start, goal in tests:
    path_bfs, transfers_bfs = metro.bfs_least_transfers(start, goal)  # en az aktarmalı rotayı bul
    path_astar, cost_astar = metro.a_star_fastest_route(start, goal)  # en hızlı rotayı bul
    fare = metro.calculate_fare(path_astar)                           # rotanın ücretini hesapla
    print(f"bşlngç: {start}")
    print(f"bitiş: {goal}")
    print(f"en az aktarmalı rota: {' -> '.join(path_bfs)} | aktarmalar: {transfers_bfs}")
    print(f"en hızlı rota: {' -> '.join(path_astar)} | süre: {cost_astar} dk | ücret: {fare} tl")
    print("-" * 100)