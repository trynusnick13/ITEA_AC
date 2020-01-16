For create HW or practise you should do:

1. `git checkout master` - переходимо на основну гілку master
2. `git pull` - забираємо зміни з віддаленого репозиторію
3. `git checkout -b {folder_name}-{your_name}` - 
створюємо нову гілку і відразу переключаємось на неї.
    * ця команда є аналогом двох команд:
        * `git branch {folder_name}-{your_name}` - створює нову гілку
        * `git checkout {folder_name}-{your_name}` - переключаємось з гілки master на нову гілку

4.  Copy necessary files from main folder (Yurii_Khomych) to your {Your_Name} 

5. `git add .` or `git add {your_file}` - Додаємо файл в стадію stage
6. `git commit -m 'Your commit message'` - Створюємо коміт з файлами з кроку 5
7. `git push -u origin {branch_name from step 3}` - Публікуємо зміни до 
віддаленого репозиторія створюючи нову гілку з назвою з кроку 3
    * при наступних комітах в цю гілку необхідно лише писати команду 
    `git push`

8. Create Pull Request from your branch_name and repository to main repo
