
# Проект по автоматизации тестирования сайта доставки еды [YAMI YAMI](https://yamiyami.ru/)

## Технологии и инструменты

<img src="images/icons/python-original.svg" width="50"> <img src="images/icons/pytest.png" width="50">
<img src="images/icons/intellij_pycharm.png" width="50"> <img src="images/icons/selene.png" width="50">
<img src="images/icons/selenium.png" width="50"> <img src="images/icons/selenoid.png" width="50">
<img src="images/icons/jenkins.png" width="50"> <img src="images/icons/allure_report.png" width="50">
<img src="images/icons/allure_testops.png" width="50"> <img src="images/icons/tg.png" width="50">
<img src="images/icons/jira.png" width="50">

> *В данном проекте написаны UI-автотесты на <code><strong>*Python*</strong></code> с использованием <code><strong>*Selene*</strong></code>.*
>
>*Запуск тестов выполняется из <code><strong>*Jenkins*</strong></code>.*
>
>*<code><strong>*Selenoid*</strong></code> используется для запуска браузера.*
>
>*<code><strong>*Allure Report, Allure TestOps, Jira, Telegram Bot*</strong></code> используются для визуализации результатов тестирования.*

## Реализованы проверки

### Auto

> - [x] *Поиск позиции в меню*
>- [x] *Заполнение адреса доставки*
>- [x] *Добавление позиции из меню в корзину*
>- [x] *Удаление позиции из корзины*
>- [x] *Заполнение формы обратной связи*

### Manual

>- [x] *Заполнение формы кандидата*
>- [x] *Переход на страничку компании в социальных сетях*

## Запуск тестов в [Jenkins](https://jenkins.autotests.cloud/job/yami-yami_test_project/)

### Параметры сборки

* `environment` - параметр определяет окружение для запуска тестов
* `comment` - комментарий

*Для запуска сборки необходимо указать значения параметров и нажать кнопку <code><strong>*Build*</strong></code>.*

<p align="center">
  <img src="images/jenkins_build_steps.png" alt="job" width="800">
</p>

*После выполнения сборки, в блоке <code><strong>*История сборок*</strong></code> напротив номера сборки появится
значок <img width="2%" title="Allure Report" src="images/icons/allure_report.png"><code><strong>*Allure
Report*</strong></code>, кликнув по которому, откроется страница с сформированным html-отчетом.*

<p align="center">
  <img src="images/allure_report.png" alt="job" width="1000">
</p>

## <img width="4%" title="Allure Report" src="images/icons/allure_report.png"> Отчет о результатах тестирования в [Allure Report](https://jenkins.autotests.cloud/job/yami-yami_test_project/2/allure/)

### Список тестов c описанием шагов и визуализацией результатов

<p align="center">
  <img src="images/allure_report_tests.png" alt="Allure Report" width="900">
</p>

## <img width="4%" title="Allure TestOPS" src="images/icons/allure_testops.png"> Интеграция с [Allure TestOps](https://allure.autotests.cloud/project/3857/dashboards)

### Основной дашборд

<p align="center">
  <img src="images/testops_dashboard.png" alt="dashboards" width="900">
</p>

### Тест-кейсы

<p align="center">
  <img src="images/testops_cases.png" alt="test cases" width="900">
</p>

## <img width="4%" title="Jira" src="images/icons/jira.png"> Интеграция с [Jira](https://jira.autotests.cloud/browse/HOMEWORK-989)

<p align="center">
  <img src="images/jira_integration.png" alt="jira" width="1000">
</p>

## <img width="4%" title="Selenoid" src="images/icons/selenoid.png"> Пример запуска теста в Selenoid

<p align="center">
  <img src="images/selenoid.gif" alt="video" width="1000">
</p>

## <img width="4%" title="Telegram" src="images/icons/tg.png"> Уведомления в Telegram

<p align="center">
  <img src="images/tg_bot.png" alt="Telegram" width="440">
</p>
