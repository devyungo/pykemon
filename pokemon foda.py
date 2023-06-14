import random as r
import time as t
import os as o

o.system('cls')

criticalrate = 6.25

class ataque:
    def __init__(self, name, tipagem, spf, atk, acc):
        self.tipagem = tipagem
        self.spf = spf
        self.atk = atk
        self.acc = acc
        self.name = name


scratch = ataque("Scratch", "normal", "physical", 40, 100)
ember = ataque("Ember", "fire", "special", 40, 100)
vinewhip = ataque("Vine Whip","grass", "physical", 45, 100)
watergun = ataque("Water Gun","water", "special", 40, 100)

class pokemon:
    def __init__(self, name, vida, nivel, speed, atk, spatk, defesa, defesasp, tipagem, tipagem2, ataque1, ataque2):
        self.name = name
        self.vida = vida
        self.nivel = nivel
        self.speed = speed
        self.atk = atk
        self.spatk = spatk
        self.defesa = defesa
        self.defesasp = defesasp
        self.tipagem = tipagem
        self.tipagem2 = tipagem2
        self.ataque1 = ataque1
        self.ataque2 = ataque2
        self.atkname1 = ataque1.name
        self.atkname2 = ataque2.name

Charmander = pokemon("Charmander", 19, 5, 12, 11, 12, 9, 11, "fire", "none", scratch, ember)
Bulbasaur = pokemon("Bulbasaur", 19, 5, 12, 11, 12, 9, 11, "grass", "poison", scratch, vinewhip)
Squirtle = pokemon("Squirtle", 19, 5, 12, 11, 12, 9, 11, "water", "none", scratch, watergun)

def atacar(atkn, ataque, defn):
    global criticalrate
    acf = r.randrange(0,100)
    if acf>ataque.acc:
        acertou=0
    else:
        acertou=1
    if ataque.tipagem == "fire" and defn.tipagem == "grass":
        multiplier = 2
    elif ataque.tipagem == "grass" and defn.tipagem == "fire":
        multiplier = 0.5
    elif ataque.tipagem == "water" and defn.tipagem == "fire":
        multiplier = 2
    elif ataque.tipagem == "fire" and defn.tipagem == "water":
        multiplier = 0.5
    elif ataque.tipagem == "grass" and defn.tipagem == "water":
        multiplier = 2
    elif ataque.tipagem == "water" and defn.tipagem == "grass":
        multiplier = 0.5
    else:
        multiplier = 1
    if ataque.spf == "special":
        atkstat = atkn.spatk
        defstat = defn.defesasp
    elif ataque.spf == "physical":
        atkstat = atkn.atk
        defstat = defn.defesa
    if ataque.tipagem == atkn.tipagem:
        stab = 1.5
    else:
        stab = 1
    crate = r.randrange(0,100)
    if crate<criticalrate:
        critical = 1.5
    else:
        critical = 1
    damage = ((((2*atkn.nivel/5+2)*atkstat*ataque.atk/defstat)/50)+2)*stab*multiplier*critical*(r.randrange(80, 100)/100)*acertou
    return damage, acertou

a12 = [1,2]

def batalha(pokemon1, pokemon2):
    global a12
    perdeu = 0
    vida1 = pokemon1.vida
    vida2 = pokemon2.vida
    while True:
        print(f"{pokemon1.name}\nVida: {vida1}/{pokemon1.vida}")
        while True:
            chooseatk = input(f"Qual ataque você gostaria de usar?\n[0]{pokemon1.atkname1}\n[1]{pokemon1.atkname2}\n")
            if chooseatk=="0" or chooseatk=="1":
                break
            else:
                print("Tente novamente")
        if chooseatk=="0":
            ataque1 = pokemon1.ataque1
        elif chooseatk=="1":
            ataque1 = pokemon1.ataque2
        damage1, acertou1 = atacar(pokemon1, ataque1, pokemon2)
        damage1 = int(damage1)
        o.system('cls')
        print(f"{pokemon2.name}\nVida: {vida2}/{pokemon2.vida}")
        while True:
            chooseatk = input(f"Qual ataque você gostaria de usar?\n[0]{pokemon2.atkname1}\n[1]{pokemon2.atkname2}\n")
            if chooseatk=="0" or chooseatk=="1":
                break
            else:
                print("Tente novamente")
        if chooseatk=="0":
            ataque2 = pokemon2.ataque1
        elif chooseatk=="1":
            ataque2 = pokemon2.ataque2
        damage2, acertou2 = atacar(pokemon2, ataque2, pokemon1)
        damage2 = int(damage2)
        o.system('cls')
        if vida1>0:
            vida2-=damage1
        else:
            perdeu = "pokemon1"
        if vida2>0:
            vida1-=damage2
        else:
            perdeu = "pokemon2"
        if perdeu == "pokemon1":
            print(f"{pokemon1.name} caiu {damage2} pontos de dano.")
            t.sleep(5)
            o.system('cls')
            break
        print(f"{pokemon1.name} acertou um {ataque1.name} e causou {damage1} pontos de dano em {pokemon2.name}.")
        t.sleep(2)
        if perdeu == "pokemon2":
            print(f"{pokemon2.name} caiu após receber {damage1} pontos de dano.")
            t.sleep(5)
            o.system('cls')
            break
        print(f"{pokemon2.name} acertou um {ataque2.name} e causou {damage2} pontos de dano em {pokemon1.name}.")
        t.sleep(4)
        o.system('cls')

def batalha2(pokemon1, pokemon2):
    if pokemon1.speed>pokemon2.speed:
        batalha(pokemon1, pokemon2)
    elif pokemon2.speed>pokemon1.speed:
        batalha(pokemon2, pokemon1)
    else:
        global a12
        choose = r.choice(a12)
        if choose == 1:
            batalha(pokemon1, pokemon2)
        else:
            batalha(pokemon2, pokemon1)

def menuchoose():
    global Charmander
    global Bulbasaur
    global Squirtle
    pokemon1 = 0
    pokemon2 = 0
    while True:
        choose1 = input("[0] Charmander\n[1] Bulbasaur \n[2] Squirtle\nQual será o primeiro pokémon?\n")
        if choose1=="0":
            pokemon1 = Charmander
            break
        elif choose1=="1":
            pokemon1 = Bulbasaur
            break
        elif choose1=="2":
            pokemon1 = Squirtle
            break
        else:
            print("Tente novamente")
    o.system('cls')
    while True:
        choose2 = input("[0] Charmander\n[1] Bulbasaur \n[2] Squirtle\nQual será o segundo pokémon?\n")
        if choose2=="0":
            pokemon2 = Charmander
            break
        elif choose2=="1":
            pokemon2 = Bulbasaur
            break
        elif choose2=="2":
            pokemon2 = Squirtle
            break
        else:
            print("Tente novamente")
    o.system('cls')
    batalha2(pokemon1, pokemon2)

def batalhafinal():
    while True:
        menuchoose()
        while True:
            simnao = input("[0] Sim\n[1] Não\nVocê deseja continuar?\n")
            if simnao == "0":
                break
            elif simnao == "1":
                break
            else:
                print("Tente Novamente")
        if simnao == "1":
            break


batalhafinal()