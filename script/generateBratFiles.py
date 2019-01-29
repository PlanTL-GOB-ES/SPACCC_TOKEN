#!/usr/bin/env python
# -*- coding: utf-8 -*

class Main(object):
	def main(self):
		self.fTools = open("tools.conf", "w")
		self.fAnnotation = open("annotation.conf", "w")
		self.fVisual = open("visual.conf", "w")
		
		#Rellena fichero tools.conf
		self.generarFicheroTools()
		#Rellena fichero annotation.conf
		self.generarFicheroAnnotation()
		#Rellena fichero visual.conf
		self.generarFicheroVisual()
		


	def generarFicheroTools(self):
		self.fTools.write("[options]\n\n")
		self.fTools.write("Tokens\t   tokenizer:whitespace\n")
		self.fTools.write("Sentences\tsplitter:newline\n")
		self.fTools.write("Validation\tvalidate:none\n")
		self.fTools.write("Annotation-log\tlogfile:<NONE>")

	def generarFicheroAnnotation(self):
		self.fAnnotation.write("[entities]\n")
		#Etiquetas adjetivos
		self.generarAdjetivos(0)

		#Etiquetas adverbios
		self.generarAdverbios(0)

		#Etiquetas determinantes
		self.generarDeterminantes(0)

		#Etiquetas nombres
		self.generarNombres(0)

		#Etiquetas verbos
		self.generarVerbos(0)

		#Etiquetas pronombres
		self.generarPronombres(0)

		#Etiquetas conjunciones
		self.generarConjunciones(0)

		#Etiquetas interjecciones
		self.generarInterjecciones(0)

		#Etiquetas preposiciones
		self.generarPreposiciones(0)

		#Etiquetas eignos de puntuación
		self.generarPuntuacion(0)

		#Etiquetas numerales
		self.generarNumerales(0)

		#Etiquetas fechas y horas
		self.generarFechasHoras(0)

		self.fAnnotation.write("\n[relations]\n")
		self.fAnnotation.write("#none\n\n")
		
		self.fAnnotation.write("[events]\n")
		self.fAnnotation.write("#none\n\n")

		self.fAnnotation.write("[attributes]\n\n")
		#Entidad médica
		self.fAnnotation.write("EM Arg:<ENTITY>")

	def generarFicheroVisual(self):
		self.fVisual.write("[labels]\n")
		self.fVisual.write("#none\n\n")

		self.fVisual.write("[drawing]\n\n")
		self.fVisual.write("SPAN_DEFAULT\tfgColor:black, bgColor:lightgreen, borderColor:darken\n")
		self.fVisual.write("ARC_DEFAULT\tcolor:black, arrowHead:triangle-5, labelArrow:triangle-5\n")
		self.fVisual.write("ATTRIBUTE_DEFAULT\tglyph:<EMPTY>\n")
		#Colores adjetivos
		self.generarAdjetivos(1)

		#Colores adverbios
		self.generarAdverbios(1)

		#Colores determinantes
		self.generarDeterminantes(1)

		#Colores nombres
		self.generarNombres(1)

		#Colores verbos
		self.generarVerbos(1)

		#Colores pronombres
		self.generarPronombres(1)

		#Colores conjunciones
		self.generarConjunciones(1)

		#Colores interjecciones
		self.generarInterjecciones(1)

		#Colores preposiciones
		self.generarPreposiciones(1)

		#Colores eignos de puntuación
		self.generarPuntuacion(1)

		#Colores numerales
		self.generarNumerales(1)

		#Colores fechas y horas
		self.generarFechasHoras(1)

	def generarAdjetivos(self, operacion):
		self.etAdjetivos = []
		categoria = "A"
		tipo = ["Q", "O"]
		color = "bgColor:#3ADF00"

		for t in tipo:
			et1 = categoria + t
			self.etAdjetivos.append(et1)

		#operacion 0: etiquetas, operacion 1: abreviaturas, operacion 2: colores
		if operacion == 0:
			self.fAnnotation.write("\nAdjetivos\n")
			for et in self.etAdjetivos:
				self.fAnnotation.write("\t" + et + "\n")
		elif operacion == 1:
			self.fVisual.write("\nAdjetivos\t" + color + "\n")
			for et in self.etAdjetivos:
				self.fVisual.write(et + "\t" + color + "\n")

	def generarAdverbios(self, operacion):
		self.etAdverbios = []
		categoria = "R"
		tipo = ["G", "N"]
		color = "bgColor:#D8F781"

		for t in tipo:
			et1 = categoria + t
			self.etAdverbios.append(et1)

		#operacion 0: etiquetas, operacion 1: abreviaturas, operacion 2: colores
		if operacion == 0:
			self.fAnnotation.write("\nAdverbios\n")
			for et in self.etAdverbios:
				self.fAnnotation.write("\t" + et + "\n")
		elif operacion == 1:
			self.fVisual.write("\nAdverbios\t" + color + "\n")
			for et in self.etAdverbios:
				self.fVisual.write(et + "\t" + color + "\n")

	def generarDeterminantes(self, operacion):
		self.etDeterminantes = []
		categoria = "D"
		tipo = ["D", "P", "T", "E", "I", "A"]
		color = "bgColor:#DA81F5"

		for t in tipo:
			et1 = categoria + t
			self.etDeterminantes.append(et1)

		#operacion 0: etiquetas, operacion 1: abreviaturas, operacion 2: colores
		if operacion == 0:
			self.fAnnotation.write("\nDeterminantes\n")	
			for et in self.etDeterminantes:
				self.fAnnotation.write("\t" + et + "\n")
		elif operacion == 1:
			self.fVisual.write("\nDeterminantes\t" + color + "\n")
			for et in self.etDeterminantes:
				self.fVisual.write(et + "\t" + color + "\n")

	def generarNombres(self, operacion):
		self.etNombres = []
		categoria = "N"
		tipo = ["C", "P"]
		color = "bgColor:#A9BCF5"

		for t in tipo:
			et1 = categoria + t
			self.etNombres.append(et1)

		#operacion 0: etiquetas, operacion 1: abreviaturas, operacion 2: colores
		if operacion == 0:
			self.fAnnotation.write("\nNombres\n")
			for et in self.etNombres:
				self.fAnnotation.write("\t" + et + "\n")
		elif operacion == 1:
			self.fVisual.write("\nNombres\t" + color + "\n")
			for et in self.etNombres:
				self.fVisual.write(et + "\t" + color + "\n")

	def generarVerbos(self, operacion):
		self.etVerbos = []
		categoria = "V"
		tipo = ["M", "A", "S"]
		color = "bgColor:#F78181"

		for t in tipo:
			et1 = categoria + t
			self.etVerbos.append(et1)

		#operacion 0: etiquetas, operacion 1: abreviaturas, operacion 2: colores
		if operacion == 0:
			self.fAnnotation.write("\nVerbos\n")
			for et in self.etVerbos:
				self.fAnnotation.write("\t" + et + "\n")
		elif operacion == 1:
			self.fVisual.write("\nVerbos\t" + color + "\n")
			for et in self.etVerbos:
				self.fVisual.write(et + "\t" + color + "\n")

	def generarPronombres(self, operacion):
		self.etPronombres = []
		categoria = "P"
		tipo = ["0", "P", "D", "X", "I", "T", "R", "E"]
		color = "bgColor:#81DAF5"

		for t in tipo:
			et1 = categoria + t
			self.etPronombres.append(et1)

		#operacion 0: etiquetas, operacion 1: abreviaturas, operacion 2: colores
		if operacion == 0:
			self.fAnnotation.write("\nPronombres\n")
			for et in self.etPronombres:
				self.fAnnotation.write("\t" + et + "\n")
		elif operacion == 1:
			self.fVisual.write("\nPronombres\t" + color + "\n")
			for et in self.etPronombres:
				self.fVisual.write(et + "\t" + color + "\n")

	def generarConjunciones(self, operacion):
		self.etConjunciones = []
		categoria = "C"
		tipo = ["C", "S"]
		color = "bgColor:#F7BE81"

		for t in tipo:
			et1 = categoria + t
			self.etConjunciones.append(et1)

		#operacion 0: etiquetas, operacion 1: abreviaturas, operacion 2: colores
		if operacion == 0:
			self.fAnnotation.write("\nConjunciones\n")
			for et in self.etConjunciones:
				self.fAnnotation.write("\t" + et + "\n")
		elif operacion == 1:
			self.fVisual.write("\nConjunciones\t" + color + "\n")
			for et in self.etConjunciones:
				self.fVisual.write(et + "\t" + color + "\n")

	def generarInterjecciones(self, operacion):
		categoria = "I"
		color = "bgColor:#F7FE2E"

		#operacion 0: etiquetas, operacion 1: abreviaturas, operacion 2: colores
		if operacion == 0:
			self.fAnnotation.write("\nInterjecciones\n")
			self.fAnnotation.write("\t" + categoria + "\n")
		elif operacion == 1:
			self.fVisual.write("\nInterjecciones\t" + color + "\n")
			self.fVisual.write(categoria + "\t" + color + "\n")

	def generarPreposiciones(self, operacion):
		categoriaTipo = "SP"
		color = "bgColor:#F3E2A9"

		#operacion 0: etiquetas, operacion 1: abreviaturas, operacion 2: colores
		if operacion == 0:
			self.fAnnotation.write("\nPreposiciones\n")
			self.fAnnotation.write("\t" + categoriaTipo + "\n")
		elif operacion == 1:
			self.fVisual.write("\nPreposiciones\t" + color + "\n")
			self.fVisual.write(categoriaTipo + "\t" + color + "\n")

	def generarPuntuacion(self, operacion):
		self.etPuntuacion = []
		categoria = "F"
		signo = ["aa", "at", "c", "ca", "ct", "d", "e", "g", "h", "ia", "it", "la", "lt", "p", "pa", "pt", "ra", "rc", "s", "t", "x", "z"]
		color = "bgColor:#BDBDBD"

		for s in signo:
			et1 = categoria + s
			self.etPuntuacion.append(et1)

		#operacion 0: etiquetas, operacion 1: abreviaturas, operacion 2: colores
		if operacion == 0:
			self.fAnnotation.write("\nPuntuacion\n")
			for et in self.etPuntuacion:
				self.fAnnotation.write("\t" + et + "\n")
		elif operacion == 1:
			self.fVisual.write("\nPuntuacion\t" + color + "\n")
			for et in self.etPuntuacion:
				self.fVisual.write(et + "\t" + color + "\n")

	def generarNumerales(self, operacion):
		self.etNumerales = []
		categoria = "Z"
		tipo = ["", "d", "m", "p", "u"]
		color = "bgColor:#FFFFFF"

		for t in tipo:
			et1 = categoria + t
			self.etNumerales.append(et1)

		#operacion 0: etiquetas, operacion 1: abreviaturas, operacion 2: colores
		if operacion == 0:
			self.fAnnotation.write("\nNumerales\n")
			for et in self.etNumerales:
				self.fAnnotation.write("\t" + et + "\n")
		elif operacion == 1:
			self.fVisual.write("\nNumerales\t" + color + "\n")
			for et in self.etNumerales:
				self.fVisual.write(et + "\t" + color + "\n")

	def generarFechasHoras(self, operacion):
		categoria = "W"
		color = "bgColor:#F4C1E3"

		#operacion 0: etiquetas, operacion 1: abreviaturas, operacion 2: colores
		if operacion == 0:
			self.fAnnotation.write("\nFechasHoras\n")
			self.fAnnotation.write("\t" + categoria + "\n")
		elif operacion == 1:
			self.fVisual.write("\nFechasHoras\t" + color + "\n")
			self.fVisual.write(categoria + "\t" + color + "\n")


if __name__ == "__main__":
    Main().main()