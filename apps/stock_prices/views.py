from django.http import JsonResponse

import yfinance as yf


def view_single_price(request, stock_id):
    '''Retorna preço da ação de uma companhia'''
    print(stock_id)
    ticker = yf.Ticker(stock_id) #('NUBR33.SA')

    info = ticker.info
    current_price = info['currentPrice']
    previous_close = info['previousClose']
    response = {
        'symbol': info['symbol'],
        'long_name': info['longName'],
        'logo_url': info['logo_url'],
        'website': info['website'],
        'current_price': f'{current_price:.2f}',
        'previous_close': previous_close,
        'value_diff': round(current_price - previous_close, 2),
        'ratio_diff': round(100 * (current_price / previous_close - 1), 2),
    }
    return JsonResponse({'data': response or False })


def view_stock_price(request, stock_ids):
    '''Retorna preço da ação de várias companhias'''
    stock_ids = stock_ids.replace('&', ' ')
    print(stock_ids)
    result = yf.Tickers(stock_ids) #('NUBR33.SA')
    response = []

    for ticker_name in result.tickers:
        info = result.tickers[ticker_name].info
        current_price = info['currentPrice']
        previous_close = info['previousClose']
        response.append({
            'symbol': info['symbol'],
            'long_name': info['longName'],
            'logo_url': info['logo_url'],
            'website': info['website'],
            'current_price': f'{current_price:.2f}',
            'previous_close': previous_close,
            'value_diff': round(current_price - previous_close, 2),
            'ratio_diff': round(100 * (current_price / previous_close - 1), 2),
        })
    return JsonResponse({'data': response or False })
