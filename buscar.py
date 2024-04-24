import pandas as pd
import unittest

def buscar_datos(*args, database):
    df = pd.DataFrame(database).T  
    for arg in args:
        df = df[df.eq(arg).any(axis=1)]  
    if len(df) == 1:
        return df.index[0]  
    else:
        return None  

database = {
    1: {
        "nombre1": "Pablo",
        "nombre2": "Diego",
        "apellido1": "Ruiz",
        "apellido2": "Picasso"
    },
    2: {
        "nombre1": "Elio",
        "apellido1": "Anci"
    },
    3: {
        "nombre1": "Elias",
        "nombre2": "Marcos",
        "nombre3": "Luciano",
        "apellido1": "Marcelo",
        "apellido2": "Gonzalez"
    }
}



def test_buscar_datos(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", database=self.database)
        self.assertEqual(resultado, 1, "La persona no fue encontrada correctamente en la base de datos")

        resultado = buscar_datos("Elio", "Anci", database=self.database)
        self.assertEqual(resultado, 2, "La persona no fue encontrada correctamente en la base de datos")

        resultado = buscar_datos("Elias", "Marcos", "Luciano", "Marcelo", "Gonzalez", database=self.database)
        self.assertEqual(resultado, 3, "La persona no fue encontrada correctamente en la base de datos")

        resultado = buscar_datos("Pablo", "Ruiz", "Diego", "Picasso", database=self.database)
        self.assertIsNone(resultado, "La función no maneja correctamente el orden de los nombres y apellidos")

if __name__ == "__main__":
    unittest.main()
