from django.contrib.gis.db import models

class Resguardo(models.Model):
    id = models.IntegerField(db_column='gid', primary_key=True)
    nombre = models.CharField(db_column='ri_resguar', max_length=150, help_text="Esto es el nombre del resguardo, que otra cosa podia ser?????")
    familias = models.SmallIntegerField(db_column='ri_numerof')
    poblacion = models.IntegerField(db_column='ri_poblaci')
    expediente = models.CharField(db_column='ri_expedie', max_length=50)
    etnia  = models.CharField(db_column='ri_etnia', max_length=150)
    resolucion = models.CharField(db_column='ri_resoluc', max_length=50)
#    ri_resol_1 = models.CharField(max_length=50)
#    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535)
#    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535)
    the_geom = models.MultiPolygonField()
    
    objects = models.GeoManager()
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        db_table = u'resguardo'

class AreaProtegida(models.Model):
    id = models.IntegerField(db_column='gid', primary_key=True)
    nombre = models.CharField(db_column='ap_nombre_', max_length=150)
    categoria = models.IntegerField(db_column='id_ap_cate')
    orden = models.IntegerField(db_column='id_inst_ti')
    shape_leng = models.DecimalField(max_digits=65535, decimal_places=65535)
    shape_area = models.DecimalField(max_digits=65535, decimal_places=65535)
    the_geom = models.MultiPolygonField()
    class Meta:
        db_table = u'area_protegida'

    objects = models.GeoManager()

