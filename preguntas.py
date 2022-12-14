import pandas as pd

def pregunta_01():
    """
    En esta función se realiza la carga de datos.
    """
    # Lea el archivo `mushrooms.csv` y asignelo al DataFrame `df`
    df = pd.read_csv('mushrooms.csv')

    # Remueva la columna `veil_type` del DataFrame `df`.
    # Esta columna tiene un valor constante y no sirve para la detección de hongos.
    df.drop(inplace= True, labels = 'veil_type', axis =1)

    # Asigne la columna `type` a la variable `y`.
    y = df["type"]

    # Asigne una copia del dataframe `df` a la variable `X`.
    X = df.copy()

    # Remueva la columna `type` del DataFrame `X`.
    X.drop('type', axis = 1, inplace = True)

    # Retorne `X` y `y`
    return X, y


def pregunta_02():
    """
    Preparación del dataset.
    """

    # Importe train_test_split
    from sklearn.model_selection import train_test_split

    # Cargue los datos de ejemplo y asigne los resultados a `X` y `y`.
    X, y = pregunta_01()

    # Divida los datos de entrenamiento y prueba. La semilla del generador de números
    # aleatorios es 123. Use 50 patrones para la muestra de prueba.
    (X_train, X_test, y_train, y_test,) = train_test_split(
        X,
        y,
        test_size=50,
        random_state=123,
    )

    # Retorne `X_train`, `X_test`, `y_train` y `y_test`
    return X_train, X_test, y_train, y_test


def pregunta_03():

    from sklearn.linear_model import LogisticRegressionCV
    from sklearn.preprocessing import OneHotEncoder
    from sklearn.pipeline import Pipeline

    # Cargue las variables.
    X_train, X_test, y_train, y_test = pregunta_02()

    # Cree un pipeline que contenga un estimador OneHotEncoder y un estimador
    # LogisticRegression con una regularización Cs=10
    pipeline = Pipeline(
        steps=[
            ("oneHotEncoder", OneHotEncoder()),
            ("logisticRegressionCV", LogisticRegressionCV(Cs=10)),
        ],
    )

    # Entrene el pipeline con los datos de entrenamiento.
    pipeline.fit(X_train, y_train)

    # Retorne el pipeline entrenado
    return pipeline


def pregunta_04():
    # Importe confusion_matrix
    from sklearn.metrics import confusion_matrix

    # Obtenga el pipeline de la pregunta 3.
    pipeline = pregunta_03()

    # Cargue las variables.
    X_train, X_test, y_train, y_test = pregunta_02()

    # Evalúe el pipeline con los datos de entrenamiento usando la matriz de confusion.
    cfm_train = confusion_matrix(
        y_true=y_train,
        y_pred=pipeline.predict(X_train),
    )

    cfm_test = confusion_matrix(
        y_true=y_test,
        y_pred=pipeline.predict(X_test),
    )

    # Retorne la matriz de confusion de entrenamiento y prueba
    return cfm_train, cfm_test
