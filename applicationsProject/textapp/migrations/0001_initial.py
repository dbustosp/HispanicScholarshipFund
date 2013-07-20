# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CategoryRegistration'
        db.create_table(u'textapp_categoryregistration', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'textapp', ['CategoryRegistration'])

        # Adding model 'Newsletter'
        db.create_table(u'textapp_newsletter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'textapp', ['Newsletter'])

        # Adding model 'New'
        db.create_table(u'textapp_new', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['textapp.Newsletter'])),
        ))
        db.send_create_signal(u'textapp', ['New'])

        # Adding model 'Applicant'
        db.create_table(u'textapp_applicant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal(u'textapp', ['Applicant'])

        # Adding M2M table for field categoriesRegistration on 'Applicant'
        db.create_table(u'textapp_applicant_categoriesRegistration', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('applicant', models.ForeignKey(orm[u'textapp.applicant'], null=False)),
            ('categoryregistration', models.ForeignKey(orm[u'textapp.categoryregistration'], null=False))
        ))
        db.create_unique(u'textapp_applicant_categoriesRegistration', ['applicant_id', 'categoryregistration_id'])

        # Adding M2M table for field news on 'Applicant'
        db.create_table(u'textapp_applicant_news', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('applicant', models.ForeignKey(orm[u'textapp.applicant'], null=False)),
            ('new', models.ForeignKey(orm[u'textapp.new'], null=False))
        ))
        db.create_unique(u'textapp_applicant_news', ['applicant_id', 'new_id'])

        # Adding model 'Apply'
        db.create_table(u'textapp_apply', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['textapp.Applicant'])),
        ))
        db.send_create_signal(u'textapp', ['Apply'])

        # Adding model 'Donation'
        db.create_table(u'textapp_donation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.BigIntegerField')()),
            ('amount', self.gf('django.db.models.fields.BigIntegerField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['textapp.Applicant'])),
        ))
        db.send_create_signal(u'textapp', ['Donation'])

        # Adding model 'Stack'
        db.create_table(u'textapp_stack', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('number', self.gf('django.db.models.fields.BigIntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'textapp', ['Stack'])


    def backwards(self, orm):
        # Deleting model 'CategoryRegistration'
        db.delete_table(u'textapp_categoryregistration')

        # Deleting model 'Newsletter'
        db.delete_table(u'textapp_newsletter')

        # Deleting model 'New'
        db.delete_table(u'textapp_new')

        # Deleting model 'Applicant'
        db.delete_table(u'textapp_applicant')

        # Removing M2M table for field categoriesRegistration on 'Applicant'
        db.delete_table('textapp_applicant_categoriesRegistration')

        # Removing M2M table for field news on 'Applicant'
        db.delete_table('textapp_applicant_news')

        # Deleting model 'Apply'
        db.delete_table(u'textapp_apply')

        # Deleting model 'Donation'
        db.delete_table(u'textapp_donation')

        # Deleting model 'Stack'
        db.delete_table(u'textapp_stack')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'textapp.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'categoriesRegistration': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['textapp.CategoryRegistration']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['textapp.New']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'textapp.apply': {
            'Meta': {'object_name': 'Apply'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['textapp.Applicant']"})
        },
        u'textapp.categoryregistration': {
            'Meta': {'object_name': 'CategoryRegistration'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'textapp.donation': {
            'Meta': {'object_name': 'Donation'},
            'amount': ('django.db.models.fields.BigIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.BigIntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['textapp.Applicant']"})
        },
        u'textapp.new': {
            'Meta': {'object_name': 'New'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['textapp.Newsletter']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'textapp.newsletter': {
            'Meta': {'object_name': 'Newsletter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'textapp.stack': {
            'Meta': {'object_name': 'Stack'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['textapp']