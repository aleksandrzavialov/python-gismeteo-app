## Проект мобильных автотестов для приложения GisMeteo на операционной системе Android


### Основные моменты
- Тест-кейсы разработаны на языке Python с использованием фреймворков Selene, Pytest. 
- Используется Allure Reports для  генерации отчетности и интерграции с системой тест-менеджмента Allure Test Ops
- Реализована интеграция с системой трекинга ошибок Jira
- Оповещение о результатах выполнения тестов приходят в Telegram
- Тесты можно запустить как локально c помощью эмулятора устройства, так и на удаленной ферме устройств с использованием CI - системы Jenkins


## Используемые технологии
<p align="center">
  <code><img width="5%" title="Python" src="images/techs/python.png"></code>
  <code><img width="5%" title="Pycharm" src="images/techs/pycharm.png"></code>
  <code><img width="5%" title="Selene" src="images/techs/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/techs/selenium.png"></code>
  <code><img width="5%" title="Pytest" src="images/techs/pytest.png"></code>
  <code><img width="5%" title="Allure Report" src="images/techs/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/techs/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/techs/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/techs/tg.png"></code>
  <code><img width="5%" title="GitHub" src="images/techs/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/techs/jenkins.png"></code>
  <code><img width="5%" title="AndroidStudio" src="images/techs/android_studio.png"></code>
  <code><img width="5%" title="Appium" src="images/techs/appium.png"></code>
  <code><img width="5%" title="BrowserStack" src="images/techs/browserstack.png"></code>
</p>

## Реализованные тест-кейсы

- Поиск города и валидация меню погоды найденного города
- Смена языка приложения
- Работа с правами приложения
- Работа с разделом избранного
- Меню "Поделиться" 

## Настройка проекта для удаленного запуска
- Создать аккаунт на browserstack и загрузить apk-файл приложения
<img src="images/screens/browserstack_load.png" alt="Browserstack"/>

- Настроить запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/azavialov-qa-guru-python-5-mobile/) и нажать "Собрать сейчас"
<img src="images/screens/jenkins_build.png" alt="Jenkins"/>

- Информация о прохождении тестов доступна в BrowserStack и Allure - отчете сборки
<img src="images/screens/browserstack_session.png" alt="Browserstack session"/>
<img src="images/screens/jenkins_allure.png" alt="Jenkins Allure report"/>

- Во вложениях Allure прикрепляются видео и скриншоты
<p><img src="images/screens/allure_attachment.png" alt="Allure Attachments"/></p>

## Настройка проекта для локального запуска

Для локального запуска:
1. Установить Git, Poetry, Pycharm
2. Клонировать репозиторий в Pycharm
3. Создать виртуальную среду командой poetry shell, для установки зависимостей запустить poetry install
4. Выбрать интерпретатор Python
5. Для работы с Browserstack задать настройки в файле config.browserstack.env.example и удалить '.example' из названия
6. Для работы с эмуляцией установить Android Studio, Appium server, Appium inspector
   - Запустить Android Studio, открыть Virtual Device Manager и скачать образ Google Pixel 4 на Android 11
   - Запустить устройство, Appim Server, Appium Inspector, настроить Desired Capabilities в Appium Inspector
7. Для выбора среды запуска либо передать аргумент context при запуске тестов из командной строки
   - env -S "context=browserstack" pytest . --alluredir allure-results/ - для запуска тестов в browserstack
   - env -S "context=emulation" pytest . --alluredir allure-results/ - для запуска тестов в эмуляторе
8. Получить Allure отчет командой allure serve


## Возможности Allure Reports
- В разделе Overview отображается сводная информация
<img src="images/screens/allure_overview.png" alt="Allure Overview"/>

- В разделе Graphs доступна статистика прохождения тест-кейсов
<img src="images/screens/allure_graphs.png" alt="Allure Graphs"/>

## Интеграция с Allure TestOps 
- После выполнения в Allure Test Ops создаются тест-кейсы с уже заполненными шагами, которые берутся из лямбда-степов внутри тест-кейсов
<img src="images/screens/test_ops_cases.png" alt="Allure Test Ops"/>
В этом же списке можно вручную добавить ручной тест-кейс

- Суммарная информация по автоматизированным и ручным кейсам доступна в дашборде
<img src="images/screens/test_ops_dashboard.png" alt="Allure Test Ops Dashboard"/>

## Интеграция с Jira
- К уже созданной в Jira задаче в разделе сьютов Allure Test Ops можно привязать тест-кейсы
<img src="images/screens/test_ops_link_cases_jira.png" alt="Link Test Ops test cases to Jira"/>

- Из раздела Launches можно привязать тестовый прогон
<img src="images/screens/test_ops_launches.png" alt="Link Test Ops launch to Jira"/>

- Тикет в Jira
<img src="images/screens/jira.png" alt="Jira"/>

## Настроена отправка отчета в Telegram

<img src="images/screens/telegram.png" alt="Telegram"/>
