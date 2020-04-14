

**Performance Test sederhana hanya bisa dilakukan di linux/unix based**
- Menggunakan apachebenchark, dengan command ab
- Mengetest server kita dengan : ab -n <jumlahrequest> -c <concurecy> http://127.0.0.1:10001/
- Dengan menggunakan parameter sebagai berikut :
  <table>
 	  <tr>
 		  <td> Nomor </td>
 		  <td> Jumlah request</td>
      <td> Konkurensi</td>
 	  </tr>
 	  <tr>
 		  <td> 1 </td>
 		  <td> 10 </td>
      <td> 1,5,10 </td>
 	  </tr>
    <tr>
      <td> 2 </td>
      <td> 50 </td>
      <td> 1,10,30,50 </td>
    </tr>
     <tr>
      <td> 3 </td>
      <td> 100 </td>
      <td> 1,10,50,100 </td>
    </tr>
   </table>
  Concurrency melambangkan user yang mengakses secara bersamaan, concurency berbeda dengan paralel, concurency adalah bagaimana satu resource dibagi ke sekian banyak request yang meminta layanan

## Hasil Performance Test

| No Test | Currency Level | Time taken for test | Complete request | Failed request | Total transferred | Request per second | Time per request | Transfer rate |
| :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| 1 | 1 | 10.155 seconds | 10 | 0 | 1360 bytes | 0.95 [#/sec] | 1055.489  ms | 0.13  Kbytes/sec |
| 2 | 5 | 8.457 seconds | 10 | 0 | 1360 bytes | 1.18 [#/sec] | 845.708 ms | 0.16  Kbytes/sec |
| 3 | 10 | 4.384 seconds | 10 | 0 | 1360 bytes | 2.20 [#/sec] | 438.427  ms | 0.30  Kbytes/sec |
| 4 | 1 | 38.349 seconds | 50 | 0 | 6528 bytes | 1.25 [#/sec] | 90.659 ms | 0.17 Kbytes/sec |
| 5 | 10 | 14.359 seconds | 50 | 0 | 2448 bytes | 1.04 [#/sec] | 798.940 ms | 0.16  Kbytes/sec |
| 6 | 30 | 27.378 seconds | 50 | 0 | 6800 bytes | 1.83 [#/sec] | 547.564   ms | 0.16  Kbytes/sec |
| 7 | 50 | 27.532 seconds | 50 | 0 | 6800 bytes | 1.82 [#/sec] | 550.648  ms | 0.16  Kbytes/sec |
| 8 | 1 | 101.537 seconds | 100 | 0 | 13600 bytes | 0.98 [#/sec] | 1015.372 ms | 0.16  Kbytes/sec |
| 9 | 10 | 62.913 seconds | 100 | 0 | 13600 bytes | 1.53 [#/sec] | 652.063 0 ms | 0.16  Kbytes/sec |
| 10 | 50 | 51.442 seconds | 100 | 0 | 13600 bytes | 1.94 [#/sec] | 514.415  ms | 0.16  Kbytes/sec |
| 11 | 100 | 71.438 seconds | 100 | 0 | 13600 bytes | 1.40 [#/sec] | 714.381  ms | 0.16  Kbytes/sec |


- ab -n 10 -c 1 http://127.0.0.1:10001/
  ![1a](https://user-images.githubusercontent.com/36990780/79158172-11165f00-7e00-11ea-8e30-472dae343a30.png)
- ab -n 10 -c  5 http://127.0.0.1:10001/
  ![1b](https://user-images.githubusercontent.com/36990780/79158254-2db29700-7e00-11ea-86fa-7d3a91d6a504.png)
- ab -n 10 -c 10 http://127.0.0.1:10001/
  ![1c](https://user-images.githubusercontent.com/36990780/79158195-1a073080-7e00-11ea-90a0-0b354964a45d.png)
- ab -n 50 -c 1 http://127.0.0.1:10001/
  ![2a](https://user-images.githubusercontent.com/36990780/79158198-1bd0f400-7e00-11ea-85a5-53606f6336b4.png)
- ab -n 50 -c 10 http://127.0.0.1:10001/
  ![2b](https://user-images.githubusercontent.com/36990780/79158200-1d022100-7e00-11ea-8f42-3a12c2f4e97d.png)
- ab -n 50 -c 30 http://127.0.0.1:10001/
  ![2c](https://user-images.githubusercontent.com/36990780/79158203-1e334e00-7e00-11ea-91d2-a1aaadad1b10.png)
- ab -n 50 -c 50 http://127.0.0.1:10001/
  ![2d](https://user-images.githubusercontent.com/36990780/79158206-1ecbe480-7e00-11ea-8980-eec63f5c2a26.png)
- ab -n 100 -c 1 http://127.0.0.1:10001/
  ![3a](https://user-images.githubusercontent.com/36990780/79158218-212e3e80-7e00-11ea-8de5-8c99c4c62cd3.png)
- ab -n 100 -c 10 http://127.0.0.1:10001/
  ![3b](https://user-images.githubusercontent.com/36990780/79158220-225f6b80-7e00-11ea-9d1f-c88934a0405f.png)
- ab -n 100 -c 50 http://127.0.0.1:10001/
  ![3](https://user-images.githubusercontent.com/36990780/79158454-926df180-7e00-11ea-8e32-bec9ad6440ee.png)
- ab -n 100 -c 100 http://127.0.0.1:10001/
  ![3d](https://user-images.githubusercontent.com/36990780/79158224-23909880-7e00-11ea-977e-2d17d0452aa6.png)
