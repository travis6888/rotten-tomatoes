# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table(u'tomatoes_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('release_year', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('critic_rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('poster', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'tomatoes', ['Movie'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table(u'tomatoes_movie')


    models = {
        u'tomatoes.movie': {
            'Meta': {'object_name': 'Movie'},
            'critic_rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'release_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['tomatoes']