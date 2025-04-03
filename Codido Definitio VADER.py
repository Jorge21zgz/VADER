import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def obtener_valor_base(tamano, equipamiento):
    """
    Retorna el valor base de la tabla según el tamaño de la unidad y su equipamiento.
    """
    tabla = {
        "E. FUEGO": {
            "LIGERA": 0.008333,
            "MOTORIZADA": 0.011111,
            "MECANIZADA": 0.013889,
            "ACORAZADA": 0.022222
        },
        "PELOTÓN": {
            "LIGERA": 0.016667,
            "MOTORIZADA": 0.022222,
            "MECANIZADA": 0.027778,
            "ACORAZADA": 0.044444
        },
        "PELOTÓN +": {
            "LIGERA": 0.025,
            "MOTORIZADA": 0.033333,
            "MECANIZADA": 0.041667,
            "ACORAZADA": 0.066667
        },
        "SECCIÓN": {
            "LIGERA": 0.05,
            "MOTORIZADA": 0.066667,
            "MECANIZADA": 0.083333,
            "ACORAZADA": 0.133333
        },
        "SECCIÓN +": {
            "LIGERA": 0.066667,
            "MOTORIZADA": 0.088889,
            "MECANIZADA": 0.111111,
            "ACORAZADA": 0.177778
        },
        "COMPAÑÍA-": {
            "LIGERA": 0.116667,
            "MOTORIZADA": 0.155556,
            "MECANIZADA": 0.194444,
            "ACORAZADA": 0.311111
        },
        "COMPAÑÍA": {
            "LIGERA": 0.15,
            "MOTORIZADA": 0.2,
            "MECANIZADA": 0.25,
            "ACORAZADA": 0.4
        },
        "COMPAÑÍA +": {
            "LIGERA": 0.183333,
            "MOTORIZADA": 0.244444,
            "MECANIZADA": 0.305556,
            "ACORAZADA": 0.488889
        }
    }
    return tabla[tamano][equipamiento]

def multiplicador_adiestramiento(adiestramiento):
    """
    Devuelve el multiplicador correspondiente al nivel de adiestramiento.
    """
    factores = {
        "Alto": 1.4,
        "Medio": 1.0,
        "Bajo": 0.7
    }
    return factores[adiestramiento]

def multiplicador_moral(moral):
    """
    Devuelve el multiplicador correspondiente al nivel de moral.
    """
    factores = {
        "Alta": 1.5,
        "Media": 1.0,
        "Baja": 0.8
    }
    return factores[moral]

def multiplicador_experiencia(experiencia):
    """
    Devuelve el multiplicador correspondiente al nivel de experiencia.
    """
    factores = {
        "Con Experiencia": 1.8,
        "Sin Experiencia": 1
    }
    return factores[experiencia]

def calcular_valor_total(tamano, equipamiento, adiestramiento, moral, experiencia):
    """
    Calcula el valor total combinando el valor base de la tabla con los multiplicadores
    de adiestramiento, moral y experiencia.
    """
    valor_base = obtener_valor_base(tamano, equipamiento)
    mult_adiestramiento = multiplicador_adiestramiento(adiestramiento)
    mult_moral = multiplicador_moral(moral)
    mult_experiencia = multiplicador_experiencia(experiencia)

    valor_total = valor_base * mult_adiestramiento * mult_moral * mult_experiencia
    return valor_total

def calcular_potcomb_relativa(params1, params2):
    """
    Recibe dos conjuntos de parámetros (cada uno con tamaño, equipamiento,
    adiestramiento, moral y experiencia) y retorna la relación entre
    sus valores totales (valor1 / valor2).
    """
    text_area.delete("1.0", tk.END)
    valor1 = calcular_valor_total(*params1)
    valor2 = calcular_valor_total(*params2)
    
    # Se evita división por cero
    if valor2 == 0:
        return 0 
    
    return valor1 / valor2

def agregar_resultado(texto):
    
    resultado = texto
    text_area.insert(tk.END, resultado)
    text_area.see(tk.END)  # Desplaza la vista al final

tabla = {
    "E. FUEGO": {
        "LIGERA": 0.008333,
        "MOTORIZADA": 0.011111,
        "MECANIZADA": 0.013889,
        "ACORAZADA": 0.022222
    },
    "PELOTÓN": {
        "LIGERA": 0.016667,
        "MOTORIZADA": 0.022222,
        "MECANIZADA": 0.027778,
        "ACORAZADA": 0.044444
    },
    "PELOTÓN +": {
        "LIGERA": 0.025,
        "MOTORIZADA": 0.033333,
        "MECANIZADA": 0.041667,
        "ACORAZADA": 0.066667
    },
    "SECCIÓN": {
        "LIGERA": 0.05,
        "MOTORIZADA": 0.066667,
        "MECANIZADA": 0.083333,
        "ACORAZADA": 0.133333
    },
    "SECCIÓN +": {
        "LIGERA": 0.066667,
        "MOTORIZADA": 0.088889,
        "MECANIZADA": 0.111111,
        "ACORAZADA": 0.177778
    },
    "COMPAÑÍA-": {
        "LIGERA": 0.116667,
        "MOTORIZADA": 0.155556,
        "MECANIZADA": 0.194444,
        "ACORAZADA": 0.311111
    },
    "COMPAÑÍA": {
        "LIGERA": 0.15,
        "MOTORIZADA": 0.2,
        "MECANIZADA": 0.25,
        "ACORAZADA": 0.4
    },
    "COMPAÑÍA +": {
        "LIGERA": 0.183333,
        "MOTORIZADA": 0.244444,
        "MECANIZADA": 0.305556,
        "ACORAZADA": 0.488889
    }
}

def update_subcategory(category_var, subcategory_var,subcategory_var2, container):
    """Actualiza los botones de subcategoría según la categoría seleccionada."""
    # Limpiar el contenedor de subcategoría
    for widget in container.winfo_children():
        widget.destroy()
    # Obtener la categoría seleccionada
    categoria = category_var.get()
    opciones = list(tabla[categoria].keys())
    # Establecer el valor por defecto (la primera opción)
    subcategory_var.set(opciones[0])
    # Crear un botón para cada opción
    for opcion in opciones:
        rb = tk.Radiobutton(container, text=opcion, variable=subcategory_var, value=opcion)
        rb.pack(anchor="w")
    
    subcategory_var2.set(opciones[0])
    # Crear un botón para cada opción
    for opcion in opciones:
        rb = tk.Radiobutton(container, text=opcion, variable=subcategory_var2, value=opcion)
        rb.pack(anchor="w")

def indices_ordenados_desc(lista):
    # Ordena los índices (0, 1, 2, ...) basándose en el valor en 'lista', en orden descendente.
    return sorted(range(len(lista)), key=lambda i: lista[i], reverse=True)

VENTAJA_CMD = ctrl.Antecedent(np.arange(1, 10, 0.01), 'VENTAJA/DESVENTAJA_CMD')


VENTAJA_CMD['muy baja'] = fuzz.trimf(VENTAJA_CMD.universe, [1, 1, 1.2])
VENTAJA_CMD['baja'] = fuzz.trimf(VENTAJA_CMD.universe, [1, 1.2, 1.5])
VENTAJA_CMD['media'] = fuzz.trimf(VENTAJA_CMD.universe, [1.2, 1.5, 2.5])
VENTAJA_CMD['alta'] = fuzz.trimf(VENTAJA_CMD.universe, [1.5, 2.5, 3.5])
VENTAJA_CMD['muy alta'] = fuzz.trapmf(VENTAJA_CMD.universe, [2.5, 3.5, 10, 10])


VENTAJA_OL = ctrl.Antecedent(np.arange(1, 30, 0.01), 'VENTAJA/DESVENTAJA_OL')


VENTAJA_OL['muy baja'] = fuzz.trimf(VENTAJA_OL.universe, [1, 1, 1.5])
VENTAJA_OL['baja'] = fuzz.trimf(VENTAJA_OL.universe, [1, 1.5, 2])
VENTAJA_OL['media'] = fuzz.trimf(VENTAJA_OL.universe, [1.5, 2, 3])
VENTAJA_OL['alta'] = fuzz.trimf(VENTAJA_OL.universe, [2, 3, 4])
VENTAJA_OL['muy alta'] = fuzz.trapmf(VENTAJA_OL.universe, [3, 4, 10, 10])

VENTAJA_OM = ctrl.Antecedent(np.arange(1, 30, 0.01), 'VENTAJA/DESVENTAJA_OM')


VENTAJA_OM['muy baja'] = fuzz.trimf(VENTAJA_OM.universe, [1, 1, 2])
VENTAJA_OM['baja'] = fuzz.trimf(VENTAJA_OM.universe, [1, 2, 3])
VENTAJA_OM['media'] = fuzz.trimf(VENTAJA_OM.universe, [2, 3, 4.5])
VENTAJA_OM['alta'] = fuzz.trimf(VENTAJA_OM.universe, [3, 4.5, 6])
VENTAJA_OM['muy alta'] = fuzz.trapmf(VENTAJA_OM.universe, [4.5, 6, 10, 10])

PROB_DEFEND= ctrl.Consequent(np.arange(0, 110, 0.01), 'PROB_DEFEND')

PROB_DEFEND['muy baja'] = fuzz.trimf(PROB_DEFEND.universe, [0, 0, 20])
PROB_DEFEND['baja'] = fuzz.trimf(PROB_DEFEND.universe, [10, 20, 40])
PROB_DEFEND['media'] = fuzz.trimf(PROB_DEFEND.universe, [30, 50, 70])
PROB_DEFEND['alta'] = fuzz.trimf(PROB_DEFEND.universe, [60, 80, 90])
PROB_DEFEND['muy alta'] = fuzz.trimf(PROB_DEFEND.universe, [80, 100, 100])

PROB_REINFORCE= ctrl.Consequent(np.arange(0, 110, 0.01), 'PROB_REINFORCE')

PROB_REINFORCE['muy baja'] = fuzz.trimf(PROB_REINFORCE.universe, [0, 0, 20])
PROB_REINFORCE['baja'] = fuzz.trimf(PROB_REINFORCE.universe, [10, 20, 40])
PROB_REINFORCE['media'] = fuzz.trimf(PROB_REINFORCE.universe, [30, 50, 70])
PROB_REINFORCE['alta'] = fuzz.trimf(PROB_REINFORCE.universe, [60, 80, 90])
PROB_REINFORCE['muy alta'] = fuzz.trimf(PROB_REINFORCE.universe, [80, 100, 100])

PROB_WITHDRAW= ctrl.Consequent(np.arange(0, 110, 0.01), 'PROB_WITHDRAW')

PROB_WITHDRAW['muy baja'] = fuzz.trimf(PROB_WITHDRAW.universe, [0, 0, 20])
PROB_WITHDRAW['baja'] = fuzz.trimf(PROB_WITHDRAW.universe, [10, 20, 40])
PROB_WITHDRAW['media'] = fuzz.trimf(PROB_WITHDRAW.universe, [30, 50, 70])
PROB_WITHDRAW['alta'] = fuzz.trimf(PROB_WITHDRAW.universe, [60, 80, 90])
PROB_WITHDRAW['muy alta'] = fuzz.trimf(PROB_WITHDRAW.universe, [80, 100, 100])

PROB_DELAY= ctrl.Consequent(np.arange(0, 110, 0.01), 'PROB_DELAY')

PROB_DELAY['muy baja'] = fuzz.trimf(PROB_DELAY.universe, [0, 0, 20])
PROB_DELAY['baja'] = fuzz.trimf(PROB_DELAY.universe, [10, 20, 40])
PROB_DELAY['media'] = fuzz.trimf(PROB_DELAY.universe, [30, 50, 70])
PROB_DELAY['alta'] = fuzz.trimf(PROB_DELAY.universe, [60, 80, 90])
PROB_DELAY['muy alta'] = fuzz.trimf(PROB_DELAY.universe, [80, 100, 100])

# Ventana principal
root = tk.Tk()
root.title('Virtual Analysis for Decision and Engagement Readiness (VADER)')
root.geometry('900x700')

# Crear un frame principal para organizar las dos columnas
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

# Variable para almacenar la selección
selecciona = tk.StringVar(value="E. FUEGO")  # Valor por defecto
selecciona1 = tk.StringVar(value="LIGERA")  # Valor por defecto
selecciona2 = tk.StringVar(value="Alto")  # Valor por defecto
selecciona3 = tk.StringVar(value="Alta")  # Valor por defecto
selecciona4 = tk.StringVar(value="Con Experiencia")  # Valor por defecto
# Crear radiobuttons
rb1 = tk.Radiobutton(root, text="E. FUEGO", variable=selecciona, value="E. FUEGO")
rb1.place(x=20,y=5)

rb2 = tk.Radiobutton(root, text="PELOTÓN", variable=selecciona, value="PELOTÓN")
rb2.place(x=20,y=25)

rb3 = tk.Radiobutton(root, text="PELOTÓN +", variable=selecciona, value="PELOTÓN +")
rb3.place(x=20,y=45)

rb4 = tk.Radiobutton(root, text="SECCIÓN", variable=selecciona, value="SECCIÓN")
rb4.place(x=20,y=65)

rb5 = tk.Radiobutton(root, text="SECCIÓN +", variable=selecciona, value="SECCIÓN +")
rb5.place(x=20,y=85)

rb6 = tk.Radiobutton(root, text="COMPAÑÍA-", variable=selecciona, value="COMPAÑÍA-")
rb6.place(x=20,y=105)

rb7 = tk.Radiobutton(root, text="COMPAÑÍA", variable=selecciona, value="COMPAÑÍA")
rb7.place(x=20,y=125)

rb8 = tk.Radiobutton(root, text="COMPAÑÍA+", variable=selecciona, value="COMPAÑÍA +")
rb8.place(x=20,y=145)

rb17 = tk.Radiobutton(root, text="LIGERA", variable=selecciona1, value="LIGERA")
rb17.place(x=20,y=170)

rb18 = tk.Radiobutton(root, text="MOTORIZADA", variable=selecciona1, value="MOTORIZADA")
rb18.place(x=20,y=190)

rb19 = tk.Radiobutton(root, text="MECANIZADA", variable=selecciona1, value="MECANIZADA")
rb19.place(x=20,y=210)

rb20 = tk.Radiobutton(root, text="ACORAZADA", variable=selecciona1, value="ACORAZADA")
rb20.place(x=20,y=230)

rb25 = tk.Radiobutton(root, text="AD_ALTO", variable=selecciona2, value="Alto")
rb25.place(x=20,y=255)

rb26 = tk.Radiobutton(root, text="AD_MEDIO", variable=selecciona2, value="Medio")
rb26.place(x=20,y=275)

rb27 = tk.Radiobutton(root, text="AD_BAJO", variable=selecciona2, value="Bajo")
rb27.place(x=20,y=295)

rb31 = tk.Radiobutton(root, text="MO_ALTA", variable=selecciona3, value="Alta")
rb31.place(x=20,y=320)

rb32 = tk.Radiobutton(root, text="MO_MEDIA", variable=selecciona3, value="Media")
rb32.place(x=20,y=340)

rb33 = tk.Radiobutton(root, text="MO_BAJA", variable=selecciona3, value="Baja")
rb33.place(x=20,y=360)

rb37 = tk.Radiobutton(root, text="CON_EXP", variable=selecciona4, value="Con Experiencia")
rb37.place(x=20,y=385)

rb38 = tk.Radiobutton(root, text="SIN_EXP", variable=selecciona4, value="Sin Experiencia")
rb38.place(x=20,y=405)

seleccione = tk.StringVar(value="E. FUEGO")  # Valor por defecto
seleccione1 = tk.StringVar(value="LIGERA")  # Valor por defecto
seleccione2 = tk.StringVar(value="Alto")  # Valor por defecto
seleccione3 = tk.StringVar(value="Alta")  # Valor por defecto
seleccione4 = tk.StringVar(value="Con Experiencia")  # Valor por defecto
# Crear radiobuttons
rb9 = tk.Radiobutton(root, text="E. FUEGO", variable=seleccione, value="E. FUEGO")
rb9.place(x=120,y=5)

rb10 = tk.Radiobutton(root, text="PELOTÓN", variable=seleccione, value="PELOTÓN")
rb10.place(x=120,y=25)

rb11 = tk.Radiobutton(root, text="PELOTÓN +", variable=seleccione, value="PELOTÓN +")
rb11.place(x=120,y=45)

rb12 = tk.Radiobutton(root, text="SECCIÓN", variable=seleccione, value="SECCIÓN")
rb12.place(x=120,y=65)

rb13 = tk.Radiobutton(root, text="SECCIÓN +", variable=seleccione, value="SECCIÓN +")
rb13.place(x=120,y=85)

rb14 = tk.Radiobutton(root, text="COMPAÑÍA-", variable=seleccione, value="COMPAÑÍA-")
rb14.place(x=120,y=105)

rb15 = tk.Radiobutton(root, text="COMPAÑÍA", variable=seleccione, value="COMPAÑÍA")
rb15.place(x=120,y=125)

rb16 = tk.Radiobutton(root, text="COMPAÑÍA+", variable=seleccione, value="COMPAÑÍA +")
rb16.place(x=120,y=145)

rb21 = tk.Radiobutton(root, text="LIGERA", variable=seleccione1, value="LIGERA")
rb21.place(x=120,y=170)

rb22 = tk.Radiobutton(root, text="MOTORIZADA", variable=seleccione1, value="MOTORIZADA")
rb22.place(x=120,y=190)

rb23 = tk.Radiobutton(root, text="MECANIZADA", variable=seleccione1, value="MECANIZADA")
rb23.place(x=120,y=210)

rb24 = tk.Radiobutton(root, text="ACORAZADA", variable=seleccione1, value="ACORAZADA")
rb24.place(x=120,y=230)

rb28 = tk.Radiobutton(root, text="AD_ALTO", variable=seleccione2, value="Alto")
rb28.place(x=120,y=255)

rb29 = tk.Radiobutton(root, text="AD_MEDIO", variable=seleccione2, value="Medio")
rb29.place(x=120,y=275)

rb30 = tk.Radiobutton(root, text="AD_BAJO", variable=seleccione2, value="Bajo")
rb30.place(x=120,y=295)

rb34 = tk.Radiobutton(root, text="MO_ALTA", variable=seleccione3, value="Alta")
rb34.place(x=120,y=320)

rb35 = tk.Radiobutton(root, text="MO_MEDIA", variable=seleccione3, value="Media")
rb35.place(x=120,y=340)

rb36 = tk.Radiobutton(root, text="MO_BAJA", variable=seleccione3, value="Baja")
rb36.place(x=120,y=360)

rb39 = tk.Radiobutton(root, text="CON_EXP", variable=seleccione4, value="Con Experiencia")
rb39.place(x=120,y=385)

rb40 = tk.Radiobutton(root, text="SIN_EXP", variable=seleccione4, value="Sin Experiencia")
rb40.place(x=120,y=405)


seleccionot = tk.StringVar(value="CMD")  # Valor por defecto


rb41 = tk.Radiobutton(root, text="OT_CMD", variable=seleccionot, value="CMD")
rb41.place(x=80,y=430)

rb42 = tk.Radiobutton(root, text="OT_OL", variable=seleccionot, value="OL")
rb42.place(x=80,y=450)

rb43 = tk.Radiobutton(root, text="OT_OM", variable=seleccionot, value="OM")
rb43.place(x=80,y=470)

# Función para mostrar la selección
def calcular():
    pot_comb_relativa =calcular_potcomb_relativa([selecciona.get(),selecciona1.get(),selecciona2.get(),selecciona3.get(),selecciona4.get()], 
                              [seleccione.get(),seleccione1.get(),seleccione2.get(),seleccione3.get(),seleccione4.get()])
    pot_comb_relativa_var.set(str(pot_comb_relativa))

    valor = pot_comb_relativa if pot_comb_relativa < 10 else 9.99
    valores=[]
    valores_nombres=["se defienda", "se refuerce", "se retire", "intente retrasarnos"]
    if seleccionot.get()=="CMD":
        
        grado_muy_baja = fuzz.interp_membership(VENTAJA_CMD.universe, VENTAJA_CMD['muy baja'].mf, valor)
        grado_baja = fuzz.interp_membership(VENTAJA_CMD.universe, VENTAJA_CMD['baja'].mf, valor)
        grado_media = fuzz.interp_membership(VENTAJA_CMD.universe, VENTAJA_CMD['media'].mf, valor)
        grado_alta = fuzz.interp_membership(VENTAJA_CMD.universe, VENTAJA_CMD['alta'].mf, valor)
        grado_muy_alta = fuzz.interp_membership(VENTAJA_CMD.universe, VENTAJA_CMD['muy alta'].mf, valor)

        agregar_resultado("***Organización del terreno CMD***\n")
        agregar_resultado("Tenemos una ventaja muy baja al "+str(round(grado_muy_baja*100,1))+"%\n")
        agregar_resultado("Tenemos una ventaja baja al "+str(round(grado_baja*100,1))+"%\n")
        agregar_resultado("Tenemos una ventaja media al "+str(round(grado_media*100,1))+"%\n")
        agregar_resultado("Tenemos una ventaja alta al "+str(round(grado_alta*100,1))+"%\n")
        agregar_resultado("Tenemos una ventaja muy alta al "+str(round(grado_muy_alta*100,1))+"%\n")
    
        agregar_resultado("******************************************************************\n")

        # DEFEND

        rule1_defend_cmd = ctrl.Rule(VENTAJA_CMD['muy alta'], PROB_DEFEND['muy baja'])
        rule2_defend_cmd = ctrl.Rule(VENTAJA_CMD['alta'], PROB_DEFEND['media'])
        rule3_defend_cmd = ctrl.Rule(VENTAJA_CMD['media'], PROB_DEFEND['alta'])
        rule4_defend_cmd = ctrl.Rule(VENTAJA_CMD['baja'], PROB_DEFEND['muy alta'])
        rule5_defend_cmd = ctrl.Rule(VENTAJA_CMD['muy baja'], PROB_DEFEND['muy alta'])

        control_system_defend_cmd = ctrl.ControlSystem([rule1_defend_cmd, rule2_defend_cmd, rule3_defend_cmd, rule4_defend_cmd, rule5_defend_cmd])
        
        fuzzy_system_defend_cmd = ctrl.ControlSystemSimulation(control_system_defend_cmd)

        fuzzy_system_defend_cmd.input['VENTAJA/DESVENTAJA_CMD'] = pot_comb_relativa

        fuzzy_system_defend_cmd.compute()

        agregar_resultado("Probabilidad de que el enemigo se defienda: "+ 
                          str(round(fuzzy_system_defend_cmd.output['PROB_DEFEND'],2))+"%\n")
        valores.append(round(fuzzy_system_defend_cmd.output['PROB_DEFEND'],2))
        # REINFORCE

        rule1_reinforce_cmd = ctrl.Rule(VENTAJA_CMD['muy alta'], PROB_REINFORCE['muy baja'])
        rule2_reinforce_cmd = ctrl.Rule(VENTAJA_CMD['alta'], PROB_REINFORCE['alta'])
        rule3_reinforce_cmd = ctrl.Rule(VENTAJA_CMD['media'], PROB_REINFORCE['muy alta'])
        rule4_reinforce_cmd = ctrl.Rule(VENTAJA_CMD['baja'], PROB_REINFORCE['alta'])
        rule5_reinforce_cmd = ctrl.Rule(VENTAJA_CMD['muy baja'], PROB_REINFORCE['media'])

        control_system_reinforce_cmd = ctrl.ControlSystem([rule1_reinforce_cmd, rule2_reinforce_cmd, rule3_reinforce_cmd, rule4_reinforce_cmd, rule5_reinforce_cmd])

        fuzzy_system_reinforce_cmd = ctrl.ControlSystemSimulation(control_system_reinforce_cmd)

        fuzzy_system_reinforce_cmd.input['VENTAJA/DESVENTAJA_CMD'] = pot_comb_relativa

        fuzzy_system_reinforce_cmd.compute()

        agregar_resultado("Probabilidad de que el enemigo se refuerce: "+
                          str(round(fuzzy_system_reinforce_cmd.output['PROB_REINFORCE'],2))+"%\n")
        valores.append(round(fuzzy_system_reinforce_cmd.output['PROB_REINFORCE'],2))
        # WITHDRAW

        rule1_withdraw_cmd = ctrl.Rule(VENTAJA_CMD['muy alta'], PROB_WITHDRAW['alta'])
        rule2_withdraw_cmd = ctrl.Rule(VENTAJA_CMD['alta'], PROB_WITHDRAW['media'])
        rule3_withdraw_cmd = ctrl.Rule(VENTAJA_CMD['media'], PROB_WITHDRAW['baja'])
        rule4_withdraw_cmd = ctrl.Rule(VENTAJA_CMD['baja'], PROB_WITHDRAW['muy baja'])
        rule5_withdraw_cmd = ctrl.Rule(VENTAJA_CMD['muy baja'], PROB_WITHDRAW['muy baja'])

        control_system_withdraw_cmd = ctrl.ControlSystem([rule1_withdraw_cmd, rule2_withdraw_cmd, rule3_withdraw_cmd, rule4_withdraw_cmd, rule5_withdraw_cmd])

        fuzzy_system_withdraw_cmd = ctrl.ControlSystemSimulation(control_system_withdraw_cmd)

        fuzzy_system_withdraw_cmd.input['VENTAJA/DESVENTAJA_CMD'] = pot_comb_relativa

        fuzzy_system_withdraw_cmd.compute()

        agregar_resultado("Probabilidad de que el enemigo se retire: "+
                          str(round(fuzzy_system_withdraw_cmd.output['PROB_WITHDRAW'],2))+"%\n")
        valores.append(round(fuzzy_system_withdraw_cmd.output['PROB_WITHDRAW'],2))
        # DELAY
        
        rule1_delay_cmd = ctrl.Rule(VENTAJA_CMD['muy alta'], PROB_DELAY['muy baja'])
        rule2_delay_cmd = ctrl.Rule(VENTAJA_CMD['alta'], PROB_DELAY['muy baja'])
        rule3_delay_cmd = ctrl.Rule(VENTAJA_CMD['media'], PROB_DELAY['baja'])
        rule4_delay_cmd = ctrl.Rule(VENTAJA_CMD['baja'], PROB_DELAY['media'])
        rule5_delay_cmd = ctrl.Rule(VENTAJA_CMD['muy baja'], PROB_DELAY['alta'])

        control_system_delay_cmd = ctrl.ControlSystem([rule1_delay_cmd, rule2_delay_cmd, rule3_delay_cmd, rule4_delay_cmd, rule5_delay_cmd])

        fuzzy_system_delay_cmd = ctrl.ControlSystemSimulation(control_system_delay_cmd)

        fuzzy_system_delay_cmd.input['VENTAJA/DESVENTAJA_CMD'] = pot_comb_relativa

        fuzzy_system_delay_cmd.compute()

        agregar_resultado("Probabilidad de que el enemigo intente retrasar: "+
              str(round(fuzzy_system_delay_cmd.output['PROB_DELAY'],2))+"%\n")
        
        valores.append(round(fuzzy_system_delay_cmd.output['PROB_DELAY'],2))
        
        valores_ordenados=indices_ordenados_desc(valores)
        
        agregar_resultado("******************************************************************\n")
        if grado_muy_baja==0 and grado_baja==0 and grado_media==0 and grado_alta==0 and grado_muy_alta==0:
            agregar_resultado("Estamos en desventaja, no debemos atacar\n")
            agregar_resultado("******************************************************************\n")
        if grado_baja>0.9:
            agregar_resultado("La ventaja que tenemos es muy pequeña, si atacamos\n"
                              "es probable que no cumplamos la misión.\n")
            agregar_resultado("******************************************************************\n")

        if grado_muy_baja==0 and grado_baja==0 and grado_media==0 and grado_alta==0 and grado_muy_alta==0:
            pass
        else:
            accion1=valores_nombres[valores_ordenados[0]]
            accion2=valores_nombres[valores_ordenados[1]]
            accion3=valores_nombres[valores_ordenados[2]]
            agregar_resultado("******************************************************************\n")
            agregar_resultado("Lo más probable es que el enemigo "+accion1+"\n"
                                "o que en su defecto "+accion2+"\n")
            agregar_resultado("******************************************************************\n")

    elif seleccionot.get()=="OL":
        grado_muy_baja = fuzz.interp_membership(VENTAJA_OL.universe, VENTAJA_OL['muy baja'].mf, valor)
        grado_baja = fuzz.interp_membership(VENTAJA_OL.universe, VENTAJA_OL['baja'].mf, valor)
        grado_media = fuzz.interp_membership(VENTAJA_OL.universe, VENTAJA_OL['media'].mf, valor)
        grado_alta = fuzz.interp_membership(VENTAJA_OL.universe, VENTAJA_OL['alta'].mf, valor)
        grado_muy_alta = fuzz.interp_membership(VENTAJA_OL.universe, VENTAJA_OL['muy alta'].mf, valor)

        agregar_resultado("***Organización del terreno OL***\n")
        agregar_resultado("Tenemos una ventaja muy baja al "+str(round(grado_muy_baja*100,1))+"%\n")
        agregar_resultado("Tenemos una ventaja baja al "+str(round(grado_baja*100,1))+"%\n")
        agregar_resultado("Tenemos una ventaja media al "+str(round(grado_media*100,1))+"%\n")
        agregar_resultado("Tenemos una ventaja alta al "+str(round(grado_alta*100,1))+"%\n")
        agregar_resultado("Tenemos una ventaja muy alta al "+str(round(grado_muy_alta*100,1))+"%\n")

        agregar_resultado("******************************************************************\n")

        # DEFEND

        rule1_defend_ol = ctrl.Rule(VENTAJA_OL['muy alta'], PROB_DEFEND['muy baja'])
        rule2_defend_ol = ctrl.Rule(VENTAJA_OL['alta'], PROB_DEFEND['media'])
        rule3_defend_ol = ctrl.Rule(VENTAJA_OL['media'], PROB_DEFEND['alta'])
        rule4_defend_ol = ctrl.Rule(VENTAJA_OL['baja'], PROB_DEFEND['muy alta'])
        rule5_defend_ol = ctrl.Rule(VENTAJA_OL['muy baja'], PROB_DEFEND['muy alta'])

        control_system_defend_ol = ctrl.ControlSystem([rule1_defend_ol, rule2_defend_ol, rule3_defend_ol, rule4_defend_ol, rule5_defend_ol])

        fuzzy_system_defend_ol = ctrl.ControlSystemSimulation(control_system_defend_ol)

        fuzzy_system_defend_ol.input['VENTAJA/DESVENTAJA_OL'] = pot_comb_relativa

        fuzzy_system_defend_ol.compute()

        agregar_resultado("Probabilidad de que el enemigo se defienda: "+
                          str(round(fuzzy_system_defend_ol.output['PROB_DEFEND'],2))+"%\n")
        valores.append(round(fuzzy_system_defend_ol.output['PROB_DEFEND'],2))

        # REINFORCE

        rule1_reinforce_ol = ctrl.Rule(VENTAJA_OL['muy alta'], PROB_REINFORCE['muy baja'])
        rule2_reinforce_ol = ctrl.Rule(VENTAJA_OL['alta'], PROB_REINFORCE['alta'])
        rule3_reinforce_ol = ctrl.Rule(VENTAJA_OL['media'], PROB_REINFORCE['muy alta'])
        rule4_reinforce_ol = ctrl.Rule(VENTAJA_OL['baja'], PROB_REINFORCE['alta'])
        rule5_reinforce_ol = ctrl.Rule(VENTAJA_OL['muy baja'], PROB_REINFORCE['media'])

        control_system_reinforce_ol = ctrl.ControlSystem([rule1_reinforce_ol, rule2_reinforce_ol, rule3_reinforce_ol, rule4_reinforce_ol, rule5_reinforce_ol])

        fuzzy_system_reinforce_ol = ctrl.ControlSystemSimulation(control_system_reinforce_ol)

        fuzzy_system_reinforce_ol.input['VENTAJA/DESVENTAJA_OL'] = pot_comb_relativa

        fuzzy_system_reinforce_ol.compute()

        agregar_resultado("Probabilidad de que el enemigo se refuerce: "
                          + str(round(fuzzy_system_reinforce_ol.output['PROB_REINFORCE'],2))+"%\n")
        valores.append(round(fuzzy_system_reinforce_ol.output['PROB_REINFORCE'],2))

        # WITHDRAW

        rule1_withdraw_ol = ctrl.Rule(VENTAJA_OL['muy alta'], PROB_WITHDRAW['alta'])
        rule2_withdraw_ol = ctrl.Rule(VENTAJA_OL['alta'], PROB_WITHDRAW['media'])
        rule3_withdraw_ol = ctrl.Rule(VENTAJA_OL['media'], PROB_WITHDRAW['baja'])
        rule4_withdraw_ol = ctrl.Rule(VENTAJA_OL['baja'], PROB_WITHDRAW['muy baja'])
        rule5_withdraw_ol = ctrl.Rule(VENTAJA_OL['muy baja'], PROB_WITHDRAW['muy baja'])

        control_system_withdraw_ol = ctrl.ControlSystem([rule1_withdraw_ol, rule2_withdraw_ol, rule3_withdraw_ol, rule4_withdraw_ol, rule5_withdraw_ol])

        fuzzy_system_withdraw_ol = ctrl.ControlSystemSimulation(control_system_withdraw_ol)

        fuzzy_system_withdraw_ol.input['VENTAJA/DESVENTAJA_OL'] = pot_comb_relativa

        fuzzy_system_withdraw_ol.compute()

        agregar_resultado("Probabilidad de que el enemigo se retire: "+
                          str(round(fuzzy_system_withdraw_ol.output['PROB_WITHDRAW'],2))+"%\n")
        valores.append(round(fuzzy_system_withdraw_ol.output['PROB_WITHDRAW'],2))

        # DELAY

        rule1_delay_ol = ctrl.Rule(VENTAJA_OL['muy alta'], PROB_DELAY['muy baja'])
        rule2_delay_ol = ctrl.Rule(VENTAJA_OL['alta'], PROB_DELAY['muy baja'])
        rule3_delay_ol = ctrl.Rule(VENTAJA_OL['media'], PROB_DELAY['baja'])
        rule4_delay_ol = ctrl.Rule(VENTAJA_OL['baja'], PROB_DELAY['media'])
        rule5_delay_ol = ctrl.Rule(VENTAJA_OL['muy baja'], PROB_DELAY['alta'])

        control_system_delay_ol = ctrl.ControlSystem([rule1_delay_ol, rule2_delay_ol, rule3_delay_ol, rule4_delay_ol, rule5_delay_ol])

        fuzzy_system_delay_ol = ctrl.ControlSystemSimulation(control_system_delay_ol)

        fuzzy_system_delay_ol.input['VENTAJA/DESVENTAJA_OL'] = pot_comb_relativa

        fuzzy_system_delay_ol.compute()

        agregar_resultado("Probabilidad de que el enemigo intente retrasar: "+
                        str(round(fuzzy_system_delay_ol.output['PROB_DELAY'],2))+"%\n")
        
        valores.append(round(fuzzy_system_delay_ol.output['PROB_DELAY'],2))
        valores_ordenados=indices_ordenados_desc(valores)
      
        agregar_resultado("******************************************************************\n")
        if grado_muy_baja==0 and grado_baja==0 and grado_media==0 and grado_alta==0 and grado_muy_alta==0:
            agregar_resultado("Estamos en desventaja, no debemos atacar\n")
            agregar_resultado("******************************************************************\n")
        if grado_baja>0.9:
            agregar_resultado("La ventaja que tenemos es muy pequeña, si atacamos\n"
                              "es probable que no cumplamos la misión.\n")
            agregar_resultado("******************************************************************\n")

        if grado_muy_baja==0 and grado_baja==0 and grado_media==0 and grado_alta==0 and grado_muy_alta==0:
            pass
        else:
            accion1=valores_nombres[valores_ordenados[0]]
            accion2=valores_nombres[valores_ordenados[1]]
            accion3=valores_nombres[valores_ordenados[2]]
            agregar_resultado("******************************************************************\n")
            agregar_resultado("Lo más probable es que el enemigo "+accion1+"\n"
                                "o que en su defecto "+accion2+"\n")
            agregar_resultado("******************************************************************\n")

    else:
        grado_muy_baja = fuzz.interp_membership(VENTAJA_OM.universe, VENTAJA_OM['muy baja'].mf, valor)
        grado_baja = fuzz.interp_membership(VENTAJA_OM.universe, VENTAJA_OM['baja'].mf, valor)
        grado_media = fuzz.interp_membership(VENTAJA_OM.universe, VENTAJA_OM['media'].mf, valor)
        grado_alta = fuzz.interp_membership(VENTAJA_OM.universe, VENTAJA_OM['alta'].mf, valor)
        grado_muy_alta = fuzz.interp_membership(VENTAJA_OM.universe, VENTAJA_OM['muy alta'].mf, valor)

        agregar_resultado("***Organización del terreno OM***\n")
        agregar_resultado("Tenemos una ventaja muy baja al "+str(round(grado_muy_baja*100,1))+"%\n")
        agregar_resultado("Tenemos una ventaja baja al "+str(round(grado_baja*100,1))+"%\n")
        agregar_resultado("Tenemos una ventaja media al "+str(round(grado_media*100,1))+"%\n")
        agregar_resultado("Tenemos una ventaja alta al "+str(round(grado_alta*100,1))+"%\n")
        agregar_resultado("Tenemos una ventaja muy alta al "+str(round(grado_muy_alta*100,1))+"%\n")

        agregar_resultado("******************************************************************\n")
        
        # DEFEND

        rule1_defend_om = ctrl.Rule(VENTAJA_OM['muy alta'], PROB_DEFEND['muy baja'])
        rule2_defend_om = ctrl.Rule(VENTAJA_OM['alta'], PROB_DEFEND['media'])
        rule3_defend_om = ctrl.Rule(VENTAJA_OM['media'], PROB_DEFEND['alta'])
        rule4_defend_om = ctrl.Rule(VENTAJA_OM['baja'], PROB_DEFEND['muy alta'])
        rule5_defend_om = ctrl.Rule(VENTAJA_OM['muy baja'], PROB_DEFEND['muy alta'])

        control_system_defend_om = ctrl.ControlSystem([rule1_defend_om, rule2_defend_om, rule3_defend_om, rule4_defend_om, rule5_defend_om])

        fuzzy_system_defend_om = ctrl.ControlSystemSimulation(control_system_defend_om)

        fuzzy_system_defend_om.input['VENTAJA/DESVENTAJA_OM'] = pot_comb_relativa

        fuzzy_system_defend_om.compute()

        agregar_resultado("Probabilidad de que el enemigo se defienda: "+
                          str(round(fuzzy_system_defend_om.output['PROB_DEFEND'],2))+"%\n")
        valores.append(round(fuzzy_system_defend_om.output['PROB_DEFEND'],2))

        # REINFORCE

        rule1_reinforce_om = ctrl.Rule(VENTAJA_OM['muy alta'], PROB_REINFORCE['muy baja'])
        rule2_reinforce_om = ctrl.Rule(VENTAJA_OM['alta'], PROB_REINFORCE['alta'])
        rule3_reinforce_om = ctrl.Rule(VENTAJA_OM['media'], PROB_REINFORCE['muy alta'])
        rule4_reinforce_om = ctrl.Rule(VENTAJA_OM['baja'], PROB_REINFORCE['alta'])
        rule5_reinforce_om = ctrl.Rule(VENTAJA_OM['muy baja'], PROB_REINFORCE['media'])

        control_system_reinforce_om = ctrl.ControlSystem([rule1_reinforce_om, rule2_reinforce_om, rule3_reinforce_om, rule4_reinforce_om, rule5_reinforce_om])

        fuzzy_system_reinforce_om = ctrl.ControlSystemSimulation(control_system_reinforce_om)

        fuzzy_system_reinforce_om.input['VENTAJA/DESVENTAJA_OM'] = pot_comb_relativa

        fuzzy_system_reinforce_om.compute()

        agregar_resultado("Probabilidad de que el enemigo se refuerce: "+
                          str(round(fuzzy_system_reinforce_om.output['PROB_REINFORCE'],2))+"%\n")
        valores.append(round(fuzzy_system_reinforce_om.output['PROB_REINFORCE'],2))

        # WITHDRAW

        rule1_withdraw_om = ctrl.Rule(VENTAJA_OM['muy alta'], PROB_WITHDRAW['alta'])
        rule2_withdraw_om = ctrl.Rule(VENTAJA_OM['alta'], PROB_WITHDRAW['media'])
        rule3_withdraw_om = ctrl.Rule(VENTAJA_OM['media'], PROB_WITHDRAW['baja'])
        rule4_withdraw_om = ctrl.Rule(VENTAJA_OM['baja'], PROB_WITHDRAW['muy baja'])
        rule5_withdraw_om = ctrl.Rule(VENTAJA_OM['muy baja'], PROB_WITHDRAW['muy baja'])

        control_system_withdraw_om = ctrl.ControlSystem([rule1_withdraw_om, rule2_withdraw_om, rule3_withdraw_om, rule4_withdraw_om, rule5_withdraw_om])

        fuzzy_system_withdraw_om = ctrl.ControlSystemSimulation(control_system_withdraw_om)

        fuzzy_system_withdraw_om.input['VENTAJA/DESVENTAJA_OM'] = pot_comb_relativa

        fuzzy_system_withdraw_om.compute()

        agregar_resultado("Probabilidad de que el enemigo se retire: "+
                          str(round(fuzzy_system_withdraw_om.output['PROB_WITHDRAW'],2))+"%\n")
        valores.append(round(fuzzy_system_withdraw_om.output['PROB_WITHDRAW'],2))

        # DELAY

        rule1_delay_om = ctrl.Rule(VENTAJA_OM['muy alta'], PROB_DELAY['muy baja'])
        rule2_delay_om = ctrl.Rule(VENTAJA_OM['alta'], PROB_DELAY['muy baja'])
        rule3_delay_om = ctrl.Rule(VENTAJA_OM['media'], PROB_DELAY['baja'])
        rule4_delay_om = ctrl.Rule(VENTAJA_OM['baja'], PROB_DELAY['media'])
        rule5_delay_om = ctrl.Rule(VENTAJA_OM['muy baja'], PROB_DELAY['alta'])

        control_system_delay_om = ctrl.ControlSystem([rule1_delay_om, rule2_delay_om, rule3_delay_om, rule4_delay_om, rule5_delay_om])

        fuzzy_system_delay_om = ctrl.ControlSystemSimulation(control_system_delay_om)

        fuzzy_system_delay_om.input['VENTAJA/DESVENTAJA_OM'] = pot_comb_relativa

        fuzzy_system_delay_om.compute()

        agregar_resultado("Probabilidad de que el enemigo intente retrasar: "+
                          str(round(fuzzy_system_delay_om.output['PROB_DELAY'],2))+"%\n")
        
        valores.append(round(fuzzy_system_delay_om.output['PROB_DELAY'],2))
        valores_ordenados=indices_ordenados_desc(valores)

        agregar_resultado("******************************************************************\n")
        if grado_muy_baja==0 and grado_baja==0 and grado_media==0 and grado_alta==0 and grado_muy_alta==0:
            agregar_resultado("Estamos en desventaja, no debemos atacar\n")
            agregar_resultado("******************************************************************\n")
        if grado_baja>0.9:
            agregar_resultado("La ventaja que tenemos es muy pequeña, si atacamos\n"
                              "es probable que no cumplamos la misión.\n")
            agregar_resultado("******************************************************************\n")

        if grado_muy_baja==0 and grado_baja==0 and grado_media==0 and grado_alta==0 and grado_muy_alta==0:
            pass
        else:
            accion1=valores_nombres[valores_ordenados[0]]
            accion2=valores_nombres[valores_ordenados[1]]
            accion3=valores_nombres[valores_ordenados[2]]
            agregar_resultado("******************************************************************\n")
            agregar_resultado("Lo más probable es que el enemigo "+accion1+"\n"
                                "o que en su defecto "+accion2+"\n")
            agregar_resultado("******************************************************************\n")

    return pot_comb_relativa 
# Botón para mostrar la selección en consola
btn = tk.Button(root, text="Calcular", command=calcular)
btn.place(x=80,y=500)

tk.Label(root,text="POTCOMB RELATIVA: ").place(x=80,y=540)
pot_comb_relativa_var = tk.StringVar()
pot_comb_relativa_var.set("0")
pot_comb_relativa_var_1=tk.Entry(root, textvariable=pot_comb_relativa_var,fg="blue", bg="yellow")
pot_comb_relativa_var_1.place(x=200,y=540,height=25, width=150)

# Crear un widget ScrolledText para mostrar resultados
text_area = ScrolledText(root, width=70, height=40)
text_area.place(x=305, y=10)


root.mainloop()

