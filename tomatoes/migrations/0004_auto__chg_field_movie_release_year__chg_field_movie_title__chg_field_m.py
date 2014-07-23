# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Movie.release_year'
        db.alter_column(u'tomatoes_movie', 'release_year', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True))

        # Changing field 'Movie.title'
        db.alter_column(u'tomatoes_movie', 'title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Movie.critic_rating'
        db.alter_column(u'tomatoes_movie', 'critic_rating', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Movie.audience_score'
        db.alter_column(u'tomatoes_movie', 'audience_score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Movie.mpaa_rating'
        db.alter_column(u'tomatoes_movie', 'mpaa_rating', self.gf('django.db.models.fields.CharField')(max_length=40, null=True))

        # Changing field 'Movie.poster'
        db.alter_column(u'tomatoes_movie', 'poster', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'Movie.runtime'
        db.alter_column(u'tomatoes_movie', 'runtime', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Movie.release_year'
        db.alter_column(u'tomatoes_movie', 'release_year', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None))

        # Changing field 'Movie.title'
        db.alter_column(u'tomatoes_movie', 'title', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'Movie.critic_rating'
        db.alter_column(u'tomatoes_movie', 'critic_rating', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None))

        # Changing field 'Movie.audience_score'
        db.alter_column(u'tomatoes_movie', 'audience_score', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None))

        # Changing field 'Movie.mpaa_rating'
        db.alter_column(u'tomatoes_movie', 'mpaa_rating', self.gf('django.db.models.fields.CharField')(default=None, max_length=40))

        # Changing field 'Movie.poster'
        db.alter_column(u'tomatoes_movie', 'poster', self.gf('django.db.models.fields.URLField')(default=None, max_length=200))

        # Changing field 'Movie.runtime'
        db.alter_column(u'tomatoes_movie', 'runtime', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=None))

    models = {
        u'tomatoes.movie': {
            'Meta': {'object_name': 'Movie'},
            'audience_score': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'critic_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpaa_rating': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'poster': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'release_year': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'runtime': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['tomatoes']