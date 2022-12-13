import re

class ExtratorURL:
    def __init__(self: object, url: str) -> None:
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self: object, url: str) -> str:
        if isinstance(url, str):
            return url.strip()
        else:
            return ''

    def valida_url(self: object) -> None:
        if not self.url:
            raise ValueError('A URL está vazia')

        padrao_url = re.compile(
            '(http(s)?://)?(www.)?bytebank.com(.br)?/cambio'
        )
        match = padrao_url.match(url)
        if not match:
            raise ValueError('A URL não é válida')

    def get_url_base(self: object) -> str:
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametro(self: object) -> str:
        indice_interrogacao = self.url.find('?')

        if indice_interrogacao:
            url_parametro = self.url[indice_interrogacao + 1 :]
            return url_parametro

    def get_valor_parametro(self: object, parametro_busca) -> int:
        indice_parametro = self.get_url_parametro().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametro().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self: object) -> int:
        return len(self.url)

    def __str__(self: object) -> str:
        return f'{self.url}\nParâmetros: {self.get_url_parametro()}\nURL Base: {self.get_url_base()}'

    def __eq__(self: object, other: str) -> bool:
        return self.url == other.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

print(f'O tamanho da URL é de {len(extrator_url)} caracteres')
print(extrator_url)

moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = extrator_url.get_valor_parametro('quantidade')

valor_dolar = 5.50

def consersao_moeda() -> None:
    if moeda_origem == 'dolar' and moeda_destino == 'real':
        conversao = int(quantidade) * valor_dolar
        print(
            f'{quantidade} dolares convertidos para real dá {conversao} reais'
        )
    elif moeda_origem == 'real' and moeda_destino == 'dolar':
        conversao = int(quantidade) // valor_dolar
        print(
            f'{quantidade} reais convertidos para dolar dá {conversao} dolares'
        )

consersao_moeda()
