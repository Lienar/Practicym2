import data_download as dd
import data_plotting as dplt
import data_calculate as dc


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")
    print("Заданы процент колебаний: от 0 до 100")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")
    threshold = input("Введите заданный процент колебаний (например, '5.23' для 5.23 процентов): ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    # Сalculate the average
    dc.calculate_and_display_average_price(stock_data)

    # Checking for exceeding the threshold
    dc.notify_if_strong_fluctuations(stock_data, threshold)

if __name__ == "__main__":
    main()
