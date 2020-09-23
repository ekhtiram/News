# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class baslik(models.Model):
	ad = models.CharField(max_length=100)

	def __str__(self):
		return self.ad

class altbaslik(models.Model):
	ad = models.CharField(max_length=100)

	def __str__(self):
		return self.ad

class ekleyen(models.Model):
	ad = models.CharField(max_length=100)

	def __str__(self):
		return self.ad

class gridapp(models.Model):
	Baslik = models.ForeignKey(baslik, on_delete=models.CASCADE, max_length=100, help_text="Başlık :")
	Alt_baslik = models.ForeignKey(altbaslik, on_delete=models.CASCADE, max_length=100, help_text="Alt Başlık :")
	Ekleyen = models.ForeignKey(ekleyen, on_delete=models.CASCADE, max_length=100, help_text="Ekleyen :")
	Icerik = models.TextField(help_text="Haber İçeriği :")
	Resim = models.FileField(upload_to='documents/', null=True, blank=False)
	Oluşturulma_Tarihi = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.Baslik

	class Meta:
		verbose_name = "Profil"
		verbose_name_plural = "Profil"
		ordering = ["-Oluşturulma_Tarihi"]
