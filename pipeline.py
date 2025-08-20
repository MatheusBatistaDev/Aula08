from etl import extrair_dados_e_consolidar, calcular_kpi_de_total_de_vendas, carregar_dados

if __name__ == "__main__":
    pasta_argumento = "data"
    df = extrair_dados_e_consolidar(pasta_argumento)
    
    if df.empty:
        print("Nenhum dado para processar.")
    else:
        df_kpi = calcular_kpi_de_total_de_vendas(df)
        formatos = ['csv', 'parquet']
        carregar_dados(df_kpi, format_saida=formatos)
        print("✅ Pipeline concluído!")
