import requests as api
import flet as ft

def main(page: ft.Page):
    page.title = "Cotação de moedas"
    page.scroll = "adaptive"

    #Campo de texto para exibir a cotação
    label = ft.Text(value="Selecione uma moeda para ver a cotação.", size=20)

    #Lista de Moedas
    moedas = ['AED-BRL', 'AED-EUR', 'AED-USD', 'AFN-USD', 'ANG-USD', 'ARS-BRL', 'ARS-CLP', 'ARS-EUR', 'ARS-PEN', 'ARS-USD', 'AUD-BRL', 'AUD-BRLPTAX', 'AUD-CHF', 'AUD-EUR', 'AUD-JPY', 'AUD-NZD', 'AUD-USD', 'BHD-EUR', 'BNB-BRL', 'BNB-EUR', 'BNB-USD', 'BOB-BRL', 'BOB-USD', 'BRETT-BRL', 'BRETT-EUR', 'BRETT-USD', 'BRL-AED', 'BRL-ARS', 'BRL-AUD', 'BRL-BBD', 'BRL-BHD', 'BRL-BOB', 'BRL-CAD', 'BRL-CHF', 'BRL-CLP', 'BRL-CNY', 'BRL-COP', 'BRL-CRC', 'BRL-CZK', 'BRL-DKK', 'BRL-EGP', 'BRL-EUR', 'BRL-GBP', 'BRL-HKD', 'BRL-HUF', 'BRL-IDR', 'BRL-ILS', 'BRL-INR', 'BRL-ISK', 'BRL-JMD', 'BRL-JOD', 'BRL-JPY', 'BRL-KES', 'BRL-KRW', 'BRL-LBP', 'BRL-LKR', 'BRL-MAD', 'BRL-MXN', 'BRL-MYR', 'BRL-NAD', 'BRL-NOK', 'BRL-NPR', 'BRL-NZD', 'BRL-OMR', 'BRL-PAB', 'BRL-PEN', 'BRL-PHP', 'BRL-PKR', 'BRL-PLN', 'BRL-PYG', 'BRL-QAR', 'BRL-RON', 'BRL-RSD', 'BRL-RUB', 'BRL-SAR', 'BRL-SEK', 'BRL-SGD', 'BRL-THB', 'BRL-TRY', 'BRL-TWD', 'BRL-USD', 'BRL-UYU', 'BRL-VEF', 'BRL-XAF', 'BRL-XAG', 'BRL-XAU', 'BRL-XCD', 'BRL-XOF', 'BRL-ZAR', 'BTC-BRL', 'BTC-EUR', 'BTC-USD', 'BYN-EUR', 'BYN-USD', 'CAD-BRL', 'CAD-BRLPTAX', 'CAD-EUR', 'CAD-JPY', 'CAD-UAH', 'CAD-USD', 'CHF-BRL', 'CHF-BRLPTAX', 'CHF-EUR', 'CHF-JPY', 'CHF-USD', 'CLP-BOB', 'CLP-BRL', 'CLP-COP', 'CLP-EUR', 'CLP-USD', 'CNY-BRL', 'CNY-EUR', 'CNY-JPY', 'CNY-USD', 'COP-BRL', 'COP-CLP', 'COP-USD', 'CRC-BRL', 'CRC-USD', 'CZK-BRL', 'CZK-USD', 'DKK-BRL', 'DKK-BRLPTAX', 'DKK-EUR', 'DKK-USD', 'DOGE-BRL', 'DOGE-EUR', 'DOGE-USD', 'EGP-BRL', 'EGP-EUR', 'EGP-USD', 'ETH-BRL', 'ETH-EUR', 'ETH-USD', 'EUR-AED', 'EUR-AFN', 'EUR-ALL', 'EUR-AMD', 'EUR-ANG', 'EUR-AOA', 'EUR-ARS', 'EUR-AUD', 'EUR-AZN', 'EUR-BAM', 'EUR-BBD', 'EUR-BDT', 'EUR-BGN', 'EUR-BHD', 'EUR-BIF', 'EUR-BND', 'EUR-BOB', 'EUR-BRL', 'EUR-BRLPTAX', 'EUR-BRLT', 'EUR-BSD', 'EUR-BWP', 'EUR-BYN', 'EUR-BZD', 'EUR-CAD', 'EUR-CHF', 'EUR-CLP', 'EUR-CNY', 'EUR-COP', 'EUR-CRC', 'EUR-CUP', 'EUR-CVE', 'EUR-CZK', 'EUR-DJF', 'EUR-DKK', 'EUR-DOP', 'EUR-DZD', 'EUR-EGP', 'EUR-ETB', 'EUR-FJD', 'EUR-GBP', 'EUR-GEL', 'EUR-GHS', 'EUR-GMD', 'EUR-GNF', 'EUR-GTQ', 'EUR-HKD', 'EUR-HNL', 'EUR-HRK', 'EUR-HTG', 'EUR-HUF', 'EUR-IDR', 'EUR-ILS', 'EUR-INR', 'EUR-IQD', 'EUR-IRR', 'EUR-ISK', 'EUR-JMD', 'EUR-JOD', 'EUR-JPY', 'EUR-KES', 'EUR-KHR', 'EUR-KRW', 'EUR-KWD', 'EUR-KYD', 'EUR-KZT', 'EUR-LAK', 'EUR-LBP', 'EUR-LKR', 'EUR-LSL', 'EUR-LYD', 'EUR-MAD', 'EUR-MDL', 'EUR-MGA', 'EUR-MKD', 'EUR-MMK', 'EUR-MOP', 'EUR-MRO', 'EUR-MUR', 'EUR-MWK', 'EUR-MXN', 'EUR-MYR', 'EUR-MZN', 'EUR-NAD', 'EUR-NGN', 'EUR-NIO', 'EUR-NOK', 'EUR-NPR', 'EUR-NZD', 'EUR-OMR', 'EUR-PAB', 'EUR-PEN', 'EUR-PGK', 'EUR-PHP', 'EUR-PKR', 'EUR-PLN', 'EUR-PYG', 'EUR-QAR', 'EUR-RON', 'EUR-RSD', 'EUR-RUB', 'EUR-RWF', 'EUR-SAR', 'EUR-SCR', 'EUR-SDG', 'EUR-SDR', 'EUR-SEK', 'EUR-SGD', 'EUR-SOS', 'EUR-STD', 'EUR-SVC', 'EUR-SYP', 'EUR-SZL', 'EUR-THB', 'EUR-TJS', 'EUR-TND', 'EUR-TRY', 'EUR-TTD', 'EUR-TWD', 'EUR-TZS', 'EUR-UAH', 'EUR-UGX', 'EUR-USD', 'EUR-UYU', 'EUR-UZS', 'EUR-VEF', 'EUR-VND', 'EUR-XAF', 'EUR-XCD', 'EUR-XOF', 'EUR-XPF', 'EUR-ZAR', 'EUR-ZMK', 'FJD-USD', 'GBP-AUD', 'GBP-BRL', 'GBP-BRLPTAX', 'GBP-CHF', 'GBP-EUR', 'GBP-JPY', 'GBP-USD', 'GBP-XCD', 'GBP-ZAR', 'GEL-EUR', 'GHS-EUR', 'GHS-USD', 'HKD-BRL', 'HKD-EUR', 'HKD-USD', 'HUF-BRL', 'HUF-EUR', 'HUF-USD', 'IDR-EUR', 'IDR-USD', 'ILS-BRL', 'ILS-EUR', 'ILS-NZD', 'ILS-USD', 'INR-BRL', 'INR-EUR', 'INR-USD', 'IQD-USD', 'IRR-USD', 'JOD-EUR', 'JOD-USD', 'JPY-BRL', 'JPY-BRLPTAX', 'JPY-EUR', 'JPY-USD', 'KES-BRL', 'KES-USD', 'KRW-BRL', 'KRW-EUR', 'KRW-USD', 'KWD-EUR', 'KWD-USD', 'KYD-USD', 'LTC-BRL', 'LTC-EUR', 'LTC-USD', 'MAD-EUR', 'MXN-BRL', 'MXN-EUR', 'MXN-USD', 'MXN-XCD', 'MYR-USD', 'NIO-USD', 'NOK-BRL', 'NOK-BRLPTAX', 'NOK-EUR', 'NOK-USD', 'NZD-BRL', 'NZD-EUR', 'NZD-ILS', 'NZD-JPY', 'NZD-USD', 'PEN-BRL', 'PEN-EUR', 'PEN-USD', 'PHP-BRL', 'PHP-USD', 'PLN-BRL', 'PLN-EUR', 'PLN-USD', 'PYG-ARS', 'PYG-BRL', 'PYG-EUR', 'PYG-USD', 'RON-BRL', 'RON-USD', 'RSD-BRL', 'RUB-BRL', 'RUB-EUR', 'RUB-USD', 'SAR-BRL', 'SAR-EUR', 'SAR-USD', 'SDG-USD', 'SEK-BRL', 'SEK-BRLPTAX', 'SEK-EUR', 'SEK-USD', 'SGD-BRL', 'SGD-EUR', 'SGD-USD', 'SOL-BRL', 'SOL-EUR', 'SOL-USD', 'SYP-USD', 'THB-BRL', 'THB-USD', 'TRY-BRL', 'TRY-EUR', 'TRY-USD', 'TWD-BRL', 'TWD-EUR', 'TWD-USD', 'UAH-USD', 'USD-AED', 'USD-AFN', 'USD-ALL', 'USD-AMD', 'USD-ANG', 'USD-AOA', 'USD-ARS', 'USD-AUD', 'USD-AZN', 'USD-BBD', 'USD-BDT', 'USD-BGN', 'USD-BHD', 'USD-BIF', 'USD-BND', 'USD-BOB', 'USD-BRL', 'USD-BRLPTAX', 'USD-BRLT', 'USD-BSD', 'USD-BWP', 'USD-BYN', 'USD-BZD', 'USD-CAD', 'USD-CHF', 'USD-CLP', 'USD-CNH', 'USD-CNY', 'USD-COP', 'USD-CRC', 'USD-CUP', 'USD-CZK', 'USD-DJF', 'USD-DKK', 'USD-DOP', 'USD-DZD', 'USD-EGP', 'USD-ETB', 'USD-EUR', 'USD-FJD', 'USD-GBP', 'USD-GEL', 'USD-GHS', 'USD-GMD', 'USD-GNF', 'USD-GTQ', 'USD-HKD', 'USD-HNL', 'USD-HRK', 'USD-HTG', 'USD-HUF', 'USD-IDR', 'USD-ILS', 'USD-INR', 'USD-IQD', 'USD-IRR', 'USD-ISK', 'USD-JMD', 'USD-JOD', 'USD-JPY', 'USD-KES', 'USD-KGS', 'USD-KHR', 'USD-KMF', 'USD-KRW', 'USD-KWD', 'USD-KYD', 'USD-KZT', 'USD-LAK', 'USD-LBP', 'USD-LKR', 'USD-LSL', 'USD-LYD', 'USD-MAD', 'USD-MDL', 'USD-MGA', 'USD-MKD', 'USD-MMK', 'USD-MNT', 'USD-MOP', 'USD-MRO', 'USD-MUR', 'USD-MVR', 'USD-MWK', 'USD-MXN', 'USD-MYR', 'USD-MZN', 'USD-NAD', 'USD-NGN', 'USD-NGNI', 'USD-NIO', 'USD-NOK', 'USD-NPR', 'USD-NZD', 'USD-OMR', 'USD-PAB', 'USD-PEN', 'USD-PGK', 'USD-PHP', 'USD-PKR', 'USD-PLN', 'USD-PYG', 'USD-QAR', 'USD-RON', 'USD-RSD', 'USD-RUB', 'USD-RWF', 'USD-SAR', 'USD-SCR', 'USD-SDG', 'USD-SEK', 'USD-SGD', 'USD-SOS', 'USD-STD', 'USD-SVC', 'USD-SYP', 'USD-SZL', 'USD-THB', 'USD-TJS', 'USD-TMT', 'USD-TND', 'USD-TRY', 'USD-TTD', 'USD-TWD', 'USD-TZS', 'USD-UAH', 'USD-UGX', 'USD-UYU', 'USD-UZS', 'USD-VEF', 'USD-VND', 'USD-VUV', 'USD-XAF', 'USD-XCD', 'USD-XOF', 'USD-XPF', 'USD-YER', 'USD-ZAR', 'USD-ZMK', 'USD-ZWL', 'UYU-BRL', 'UYU-USD', 'VEF-BRL', 'VEF-EUR', 'VEF-USD', 'VND-USD', 'XAG-BRL', 'XAG-EUR', 'XAG-USD', 'XAGG-EUR', 'XAGG-USD', 'XAU-BRL', 'XAU-EUR', 'XAU-USD', 'XBR-USD', 'XCD-GBP', 'XCD-USD', 'XOF-USD', 'XPF-EUR', 'XPF-USD', 'XRP-BRL', 'XRP-EUR', 'XRP-USD', 'ZAR-BRL', 'ZAR-EUR', 'ZAR-USD']

    #Dropdown para selecionar uma moeda
    dropdown_moedas = ft.Dropdown(
        label="Escolha a moeda",
        options=[ft.dropdown.Option(moeda) for moeda in moedas],
        width=200,
    )
    #Função para selecionar as moedas de maneira mais prática
    def selecionar_moeda(e):
        moeda = dropdown_moedas.value
        if moeda:
            #Alterei para incluir todas as moedas e não converter somente para BRL
            link = f"https://economia.awesomeapi.com.br/json/last/{moeda}"
            try:
                dados = api.get(link)
                if dados.status_code == 200:
                    data = dados.json()
                    moeda_key = list(data.keys())[0]
                    valor = data[moeda_key]['bid']
                    #Aparecer todo tipo de conversão, sem estar presso no BRL(real) - Liandro
                    label.value = f"1 {moeda} = {valor} {moeda.split("-")[1]}"
                else:
                    label.value = "Erro ao obter cotação"
            except Exception as ex:
                label.value = f"Erro: {str(ex)}"
        page.update()

    dropdown_moedas.on_change = selecionar_moeda

    # Adiciona os componentes na página
    page.add(
        ft.Column(
            [
                label,
                dropdown_moedas
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(target=main)
