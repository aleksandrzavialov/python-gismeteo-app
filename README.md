## Проект мобильных автотестов для приложение GisMeteo на операционной системе Android


### Основные моменты
<p>- Тест-кейсы разработаны на языке Python с использованием фреймворков Selene, Pytest. 
<p>- Используется Allure Reports для  генерации отчетности и интерграции с системой тест-менеджмента Allure Test Ops
<p>- Реализована интеграция с системой трекинга ошибок Jira
<p>- Оповещение о результатах выполнения тестов приходят в Telegram
<p>- Тесты можно запустить как локально c помощью эмулятора устройства, так и на удаленной ферме устройств с использованием CI - системы Jenkins


## Используемые технологии
<p  align="center">
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo_stacks/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="AndroidStudio" src="images/logo/android_studio.png"></code>
  <code><img width="5%" title="Appium" src="images/logo/appium.png"></code>
  <code><img width="5%" title="BrowserStack" src="images/logo/browserstack.png"></code>
</p>

## Реализованные тест-кейсы

- Поиск города и валидация меню погоды найденного города
- Смена языка приложения
- Работа с правами приложения
- Работа с разделом избранного
- Меню "Поделиться" 

## Настройка проекта для удаленного запуска
- Создать аккаунт на browserstack.com и загрузить apk-файл приложения <img src="images/screens/browserstack_load.png" alt="Browserstack"/>

- Настроить запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/azavialov-qa-guru-python-5-mobile/) и нажать "Собрать сейчас"
<p><img src="images/screens/jenkins_build.png" alt="Jenkins"/></p>

- Информация о прохождении тестов доступна в BrowserStack и Allure - отчете сборки
<p><img src="images/screens/browserstack_session.png" alt="Browserstack session"/></p>
<p><img src="images/screens/jenkins_allure.png" alt="Jenkins Allure report"/></p>

- Во вложениях Allure отчетах прикрепляются видео и скриншоты
<p><img src="images/screenshots/allure_attachment.png" alt="Allure Attachments"/></p>

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
7. Для выбора среды запуска либо передать аргумент context при запуске тестов из командной стройки
env -S "context=browserstack" pytest . --alluredir allure-results/ - для запуска тестов в browserstack
env -S "context=emulation" pytest . --alluredir allure-results/ - для запуска тестов в эмуляторе
8 Получить Allure отчет командой allure serve


## Возможности Allure Reports
- В разделе Overview отображается сводная информация
<img src="images/screens/allure_overview.png" alt="Allure Overview"/>
- В разделе Graphs доступна статистика прохождения тест-кейсов
<img src="images/screens/allure_graphs.png" alt="Allure Graphs"/>

## Интеграция с Allure TestOps 
После выполнения в Allure Test Ops создаются тест-кейсы с уже заполненными шагами, которые берутся из лямбда-степов внутри тест-кейсов
<img src="images/screens/test_ops_cases.png" alt="Allure Test Ops"/>
В этом же списке можно вручную добавить ручной тест-кейс
Суммарная информация по автоматизированным и ручным кейсам доступна в дашборде
<img src="images/screens/test_ops_dashboard.png" alt="Allure Test Ops Dashboard"/>

## Интеграция с Jira
К уже созданной в Jira задаче в разделе сьютов Allure Test Ops можно привязать тест-кейсы
<img src="images/screens/test_ops_dashboard.png" alt="Link Test Ops test cases to Jira"/>
Из раздела Launches можно привязать тестовый прогон
<img src="images/screens/test_ops_launches.png" alt="Link Test Ops launch to Jira"/>

## Настроена отправка отчета в Telegram

<img src="images/screens/Ttelegram.png" alt="Telegram"/>

