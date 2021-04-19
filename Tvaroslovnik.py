#!/usr/local/bin/python
# coding: windows-1250
import os
import operator

import numpy as np

import mysql_connection as db
from Dokument import Dokument

connection = db.open_connection()
mycursor = connection.cursor()


def get_ids_of_form(word):
    sql_expression = "SELECT idSlovo, tvar FROM tvar WHERE tvar = %s"
    mycursor.execute(sql_expression, (word,))
    myresult = mycursor.fetchall()
    filtered_result = set()
    for pair in myresult:
        if word == pair[1]:
            filtered_result.add(pair[0])
    return filtered_result


def ids_to_string_comma(ids):
    string = ""
    countdown = len(ids)
    for id in ids:
        string = string + str(id)
        countdown -= 1
        if countdown > 0:
            string = string + ','
    return string


def get_lemma(word):
    if word == '§':
        return word
    string_of_ids = ids_to_string_comma(get_ids_of_form(word))
    sql_expression = "SELECT DISTINCT (CAST(tvar AS CHAR CHARACTER SET utf8) COLLATE utf8_bin) from tvar " \
                     "where ( idSlovo IN (%s) " \
                     "AND ( (idTvar=0 AND slovnyDruh<>1) OR (idTvar=1))) LIMIT 1"

    mycursor.execute(sql_expression, (string_of_ids,))
    myresult = mycursor.fetchone()
    if myresult:
        return myresult[0]
    else:
        string_of_ids = ids_to_string_comma(get_ids_of_form(word.casefold()))
        sql_expression = "SELECT DISTINCT (CAST(tvar AS CHAR CHARACTER SET utf8) COLLATE utf8_bin) from tvar " \
                         "where ( idSlovo IN (%s) " \
                         "AND ( (idTvar=0 AND slovnyDruh<>1) OR (idTvar=1))) LIMIT 1"
        mycursor.execute(sql_expression, (string_of_ids,))
        myresult = mycursor.fetchone()

        if myresult:
            return myresult[0]
    return word


def lemmatize(file_name):
    lemmas = []
    bad_suffixes = (",", ".", ":", "!", "?", "-", "_")
    # opening the text file
    with open(file_name, 'r', encoding="utf-8") as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                # displaying the words
                if word.endswith(bad_suffixes):
                    word = word[:-1]
                if len(word) > 0 and (not word.endswith(bad_suffixes)):
                    lemma = get_lemma(word)
                    lemmas.append(lemma)
        file.close()
    return lemmas


def n_grams_file(file_name, n, n_grams_count):
    lemmas = lemmatize(file_name)
    if n > len(lemmas):
        return
    for i in range(len(lemmas) - n + 1):
        lemma = lemmas[i]
        for j in range(1, n):
            lemma = lemma + " " + lemmas[j + i]
        if lemma in n_grams_count:
            n_grams_count[lemma] = n_grams_count.get(lemma) + 1
        else:
            n_grams_count[lemma] = 1


def ngrams(directory, n):
    n_grams_count = {}
    number_of_documents = len(os.listdir(directory))
    for file_name in os.listdir(directory):
        print(file_name + " ...... ostava " + str(number_of_documents))
        n_grams_file(directory + "/" + file_name, n, n_grams_count)
        number_of_documents -= 1

    sorted_n_grams = dict(sorted(n_grams_count.items(), key=operator.itemgetter(1), reverse=True))
    return sorted_n_grams


def get_all_words(file_name):
    words = []
    bad_suffixes = (",", ".", ":", "!", "?", "-", "_")
    # opening the text file
    with open(file_name, 'r', encoding="utf-8") as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                # displaying the words
                if word.endswith(bad_suffixes):
                    word = word[:-1]
                if len(word) > 0 and (not word.endswith(bad_suffixes)):
                    words.append(word)
        file.close()
    return words


def n_grams_file_without_lemmatization(file_name, n, n_grams_count):
    words = get_all_words(file_name)
    if n > len(words):
        return
    for i in range(len(words) - n + 1):
        word = words[i]
        for j in range(1, n):
            word = word + " " + words[j + i]
        if word in n_grams_count:
            n_grams_count[word] = n_grams_count.get(word) + 1
        else:
            n_grams_count[word] = 1


def ngrams_without_lemmatization(directory, n):
    n_grams_count = {}
    number_of_documents = len(os.listdir(directory))
    for file_name in os.listdir(directory):
        print(file_name + " ...... ostava " + str(number_of_documents))
        n_grams_file_without_lemmatization(directory + "/" + file_name, n, n_grams_count)
        number_of_documents -= 1
    sorted_n_grams = dict(sorted(n_grams_count.items(), key=operator.itemgetter(1), reverse=True))
    return sorted_n_grams


def dict_difference(dict_a, dict_b):
    temp_a = dict_a.copy()
    temp_b = dict_b.copy()
    all(map(temp_a.pop, temp_b))
    return temp_a


def dict_difference(dict_a, dict_b):
    temp_a = dict_a.copy()
    temp_b = dict_b.copy()
    all(map(temp_a.pop, temp_b))
    return temp_a


def slova(atribut, hodnota):
    subory = []
    for file in os.listdir("dataset_test"):
        if file.endswith(".json"):
            subory.append(file)

    sql_expression = "SELECT subor FROM data WHERE " + atribut + " = " + str(hodnota) + ""
    mycursor.execute(sql_expression)
    myresult = mycursor.fetchall()
    pole = np.asarray(myresult)
    rozhodnutia = []
    for x in pole:
        if str(x)[2:][: - 2] + ".json" in subory:
            rozhodnutia.append(str(x)[2:][: - 2] + ".json")
    slova = {}
    vyskyt = {}
    normovane_slova = {}
    normovane_vyskyt = {}
    for p in rozhodnutia:
        slovaVRozhodnuti = []
        rozhodnutie = Dokument(p)
        array = rozhodnutie.naSlova_json()
        for x in array:
            s = get_lemma(str(x))
            if len(x) > 2:
                if s in slova:
                    slova[s] += 1
                    if s not in slovaVRozhodnuti:
                        slovaVRozhodnuti.append(s)
                else:
                    slova[s] = 1
        for y in slovaVRozhodnuti:
            if y in vyskyt:
                vyskyt[y] += 1
            else:
                vyskyt[y] = 1
    sorted_slova = dict(sorted(slova.items(), key=operator.itemgetter(1), reverse=True))
    sorted_vyskyt = dict(sorted(vyskyt.items(), key=operator.itemgetter(1), reverse=True))

    for x in sorted_vyskyt:
        # podiel = sorted_vyskyt[x] / len(pole)
        # if podiel > 0.5:
        normovane_vyskyt[x] = 100*(sorted_vyskyt[x] / len(pole))

    for x in sorted_slova:
        if x in normovane_vyskyt:
            normovane_slova[x] = sorted_slova[x] / len(pole)

    return (normovane_slova, normovane_vyskyt)


def bigramy(atribut, hodnota):
    subory = []
    for file in os.listdir("dataset_json"):
        if file.endswith(".json"):
            subory.append(file)
    sql_expression = "SELECT subor FROM data WHERE " + atribut + " = " + str(hodnota) + ""
    mycursor.execute(sql_expression)
    myresult = mycursor.fetchall()
    pole = np.asarray(myresult)
    rozhodnutia = []

    for x in pole:
        if str(x)[2:][: - 2] + ".json" in subory:
            rozhodnutia.append(str(x)[2:][: - 2] + ".json")
    bigramy = {}
    for p in rozhodnutia:

        rozhodnutie = Dokument(p)
        array = rozhodnutie.naSlova_json()
        for x, _ in enumerate(array):
            if x != len(array) - 1:
                prve = get_lemma(str(array[x]))
                druhe = get_lemma(str(array[x + 1]))
                bigram = "" + prve + " " + druhe
                if bigram in bigramy:
                    bigramy[str(bigram)] += 1
                else:
                    bigramy[str(bigram)] = 1
    sorted_d = dict(sorted(bigramy.items(), key=operator.itemgetter(1), reverse=True))
    print(sorted_d)
    return sorted_d

# print(ngrams("datasetUTF8", 1)) # unigramy lematizaciou...ked chces bigramy daj dvojku ako druhy parameter
# print(ngrams_without_lemmatization("datasetUTF8", 1)) # unigramy bez lematizacie
