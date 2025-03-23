# AkbankPythonveYapayZekayaGirisBootcamp
 Raylı sistemlerle ulaşım üzerine, pythonla geliştirilmiştir. 
Bu proje, bir metro ağında iki istasyon arasındaki en hızlı ve en az aktarmalı rotayı bulan bir simülasyon geliştirmeyi amaçlamaktadır. Kullanılan algoritmalar BFS (Breadth-First Search) ve A* (A-star) algoritmalarıdır. Bu algoritmalara ayrıca değineceğiz.

Kullanılan Teknolojiler ve Kütüphaneler
Python : Proje Python dilinde yazılmıştır.

heapq: A* algoritmasında kullanılan öncelik kuyruğunu oluşturmak için kullanılmıştır.

collections: BFS algoritmasında kuyruk yapısını oluşturmak için kullanılmıştır.

typing: Fonksiyon parametreleri ve dönüş değerlerinin tiplerini belirtmek için kullanılmıştır.

Algoritmaların Çalışma Mantığı
BFS Algoritması
BFS algoritması, en kısa yolu bulmak için kullanılan temel algoritmalardan biridir. Bu projede, en az aktarmalı rotayı bulmak için kullanılmıştır.

Başlangıç istasyonundan komşu istasyonlara doğru genişleyerek tüm istasyonlar arasında geçiş yapar.

Aktarma yapılan her yeni hattın sayısı takip edilir.

Rotanın sonunda hedef istasyona ulaşıldığında, rotanın aktarma sayısı ve ücret hesaplanır. 

A* Algoritması
A* Algoritması, en hızlı yolu bulmak için kullanılan bir algoritmadır. Projemizde, bu algoritma toplam tahmini süreyi minimize etmek için kullanılmaktadır.

Başlangıç istasyonundan hedefe olan en hızlı rotayı bulmak için, her komşu istasyona geçişi ve süreyi hesaplar.

Öncelik kuyruğu (heapq) kullanarak en kısa süreyi bulur ve rotayı optimize eder.

Neden Bu Algoritmaları Kullandık?
BFS, her hattı bir aktarma olarak kabul ederek en az aktarmalı rotayı bulmada oldukça etkilidir.

A*, tahmin edilen süreyi ve rotanın toplam süresini optimize ederek daha hızlı ve verimli bir çözüm sunar.

Projeyi Geliştirme Fikirleri
En hızlı rota, en az aktarmalı rota ve en az ücretli(ucuz) rota arasında tercih yaptırılabilir. Mesela ilk aklıma gelen şey, 2 aktarmalı (35tl) 35 dakikalık bir rotadansa 3 aktarmalı 20 dakikalık  (40tl) bir rotanın bizim için daha mantıklı olabileceğini tavsiye etsin. Bunun içinde bir normalizasyon algoritması ile karar verme algoritması yazılabilinir.

Görselleştirme ekleyerek kullanıcıların rotalarını harita üzerinde görsel olarak takip etmeleri sağlanabilir.

Projeyi daha da geliştirmek isterdim ama geliştireyim derken  bambaşka noktalara geldim, tabiri caizse en son geldiğim noktada ben buraya nerden geldim diye sorgulamaya başladım :) keyifli bir çalışmaydı . Arz ederim:))
