

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
| 1 | 1 | 0.142 seconds | 10 | 0 | 1350 bytes | 70.51 [#/sec] | 14.183 ms | 9.30 Kbytes/sec |
| 2 | 5 | 0.148 seconds | 10 | 0 | 1350 bytes | 67.36 [#/sec] | 74.227 ms | 8.88 Kbytes/sec |
| 3 | 10 | 0.425 seconds | 10 | 0 | 1350 bytes | 23.55 [#/sec] | 424.570 ms | 3.11 Kbytes/sec |
| 4 | 1 | 4.533 seconds | 50 | 0 | 6750 bytes | 11.03 [#/sec] | 90.659 ms | 1.45 Kbytes/sec |
| 5 | 10 | 6.130 seconds | 50 | 0 | 6750 bytes | 8.16 [#/sec] | 1226.024 ms | 1.08 Kbytes/sec |
| 6 | 30 | 8.045 seconds | 50 | 0 | 6750 bytes | 6.22 [#/sec] | 4826.780 ms | 0.82 Kbytes/sec |
| 7 | 50 | 10.524 seconds | 50 | 0 | 6750 bytes | 4.75 [#/sec] | 210.485 ms | 0.63 Kbytes/sec |
| 8 | 1 | 33.267 seconds | 100 | 0 | 13500 bytes | 3.01 [#/sec] | 332.671 ms | 0.40 Kbytes/sec |
| 9 | 10 | 32.351 seconds | 100 | 0 | 13500 bytes | 3.09 [#/sec] | 3235.090 ms | 0.41 Kbytes/sec |
| 10 | 50 | 73.526 seconds | 100 | 0 | 13500 bytes | 1.36 [#/sec] | 36763.071 ms | 0.18 Kbytes/sec |
| 11 | 100 | 120.469 seconds | 100 | 0 | 13500 bytes | 0.83 [#/sec] | 120469.454 ms | 0.11 Kbytes/sec |

##

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
