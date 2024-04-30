import tkinter as tk

def calcular():
    try:
        # Obtenha os valores dos campos de entrada
        lpa_valor = float(lpa_entry.get())
        payout_valor = float(payout_entry.get())
        dy_valor = float(dy_entry.get())

        # Realize o cálculo
        dpa = lpa_valor * (payout_valor / 100)
        preco_teto = (100 * dpa) / dy_valor

        # Formate os resultados para exibir apenas dois dígitos após o ponto decimal
        dpa_formatado = round(dpa, 2)
        preco_teto_formatado = round(preco_teto, 2)

        # Atualize os rótulos com o resultado
        resultado_dpa.config(text=f"Dividendo por Ação (DPA): {dpa_formatado}")
        resultado_preco_teto.config(text=f"Preço teto: {preco_teto_formatado}")
    except ValueError:
        # Se houver um erro ao converter para float
        resultado_dpa.config(text="Valores inválidos")

# Cria uma instância da janela
janela = tk.Tk()
janela.title("Calculadora Preço Teto")

# Cria os campos de entrada
lbl_lpa = tk.Label(janela, text="Lucro por Ação (LPA)")
lbl_lpa.pack()
lpa_entry = tk.Entry(janela)
lpa_entry.pack()

lbl_payout = tk.Label(janela, text="Payout")
lbl_payout.pack()
payout_entry = tk.Entry(janela)
payout_entry.pack()

lbl_dy = tk.Label(janela, text="Dividendo Yield Desejado")
lbl_dy.pack()
dy_entry = tk.Entry(janela)
dy_entry.pack()

# Cria o botão de cálculo
calcular_btn = tk.Button(janela, text="Calcular", command=calcular)
calcular_btn.pack()

# Cria os rótulos para exibir os resultados
resultado_dpa = tk.Label(janela, text="")
resultado_dpa.pack()

resultado_preco_teto = tk.Label(janela, text="")
resultado_preco_teto.pack()

# Inicia o loop de eventos
janela.mainloop()