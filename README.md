# Password-Generator
A simple password generator using Hexadecimal

|                |One Round                      |Two Rounds                  |
|----------------|-------------------------------|-----------------------------|
|EFF Dice (3)        |>20 years `b65c9604db2aeb748743ec0ec3f4fd5df48e801a6ba25c654b946b529b`|>100 years ` b60dc40c9e66ba417881bf25b3f4cb17cd35402756b030744d5378949821c2a4b312b2f1f4baa6f52bb78918e74a7e84c211db23d9274688e568`|
|Random (regular password)          |~10 years `a45c861cd83dfc71`   |>15 years    `b50fc40c9f66bb74782bbe2ab0f3cb1c`        |

You should probably use this with a password manager, and you should probably edit it in order to add capital letters, symbols (#$%^&*!₺), and other things.
You can also edit the hex block (this uses a 512 byte hex block, but can work with 6,144 bytes from experience, though hypothetically could work with more) but it only affects longer text.
Here are some examples of passwords possible:

 - Password1! -> 84@#.5c861cd83dfc712d44#!
 - password -> {}845c86**_1cd83df())c712d44.:.
 - lemurpasscode! -> b#8609c."22d52ceb8")46f82f22ab3b1(.

It is recommended to grab two or three words from the EFF dice list, preferably from the long list.
