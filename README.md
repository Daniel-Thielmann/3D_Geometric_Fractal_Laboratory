# Fractal ML Project

## Descrição

Este projeto visa gerar formas geométricas fractalizadas e evoluí-las utilizando **Machine Learning** e **o Método de Euler**. As imagens são geradas, treinadas e transformadas dinamicamente em novas formas fractais, permitindo exploração interativa em **3D**.

# Fractal Visualization

![Fractal Figure](/data/Figure_1.png)

## Objetivos

- Criar um **gerador de fractais** dinâmico.
- Utilizar o **método de Euler** para evoluir os fractais.
- Treinar uma **rede neural** (Autoencoder) para aprender padrões fractais e gerar novas formas.
- Criar um **visualizador interativo em 3D** para exploração das formas geradas.

## Estrutura do Projeto

```
fractal_ml_project/
│── main.py                # Arquivo principal para rodar o projeto
│── requirements.txt        # Dependências do projeto
│
├── src/                    # Código-fonte do projeto
│   ├── fractal_generator.py  # Gera fractais (Passo 1)
│   ├── euler_method.py      # Evolui fractais (Passo 2)
│   ├── ml_model.py         # ML para gerar fractais (Passo 3)
│   ├── visualize_3d.py      # Visualizador interativo (Passo 4)
│
├── data/                    # Dataset de fractais gerados
│   ├── fractals.npy         # Arquivo de dados para treino da ML
│
└── models/                  # Modelos treinados de Machine Learning
    ├── autoencoder.h5       # Modelo Autoencoder treinado
    ├── gan_generator.h5     # Modelo GAN (se implementado)
```

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/fractal_ml_project.git
   cd fractal_ml_project
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Uso

Para rodar o projeto, execute:

```sh
python main.py
```

Selecione uma das opções:

1. Gerar Fractal
2. Evoluir Fractal com Euler
3. Treinar ML para Gerar Fractais
4. Visualizar em 3D

## Dependências

- `numpy`
- `matplotlib`
- `tensorflow`
- `keras`
- `plotly`
- `scipy`

## Melhorias Futuras

- Treinar um **GAN** para gerar fractais ainda mais complexos.
- Implementar **Three.js** para uma visualização 3D em WebGL.
- Adicionar **parâmetros dinâmicos** para exploração em tempo real.
