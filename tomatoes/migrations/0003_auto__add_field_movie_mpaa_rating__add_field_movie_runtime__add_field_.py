# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Movie.mpaa_rating'
        db.add_column(u'tomatoes_movie', 'mpaa_rating',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=40),
                      keep_default=False)

        # Adding field 'Movie.runtime'
        db.add_column(u'tomatoes_movie', 'runtime',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Movie.audience_score'
        db.add_column(u'tomatoes_movie', 'audience_score',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Movie.mpaa_rating'
        db.delete_column(u'tomatoes_movie', 'mpaa_rating')

        # Deleting field 'Movie.runtime'
        db.delete_column(u'tomatoes_movie', 'runtime')

        # Deleting field 'Movie.audience_score'
        db.delete_column(u'tomatoes_movie', 'audience_score')


    models = {
        u'tomatoes.movie': {
            'Meta': {'object_name': 'Movie'},
            'audience_score': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'critic_rating': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpaa_rating': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'poster': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'release_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'runtime': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['tomatoes']