"""Main module."""

# Thanks to the Airflow Docs for creating a plugin example -
# https://airflow.apache.org/docs/apache-airflow/stable/plugins.html#example

# This is the class you derive to create a plugin
from airflow.plugins_manager import AirflowPlugin

from flask import Blueprint
from flask_appbuilder import expose, BaseView as AppBuilderBaseView


from flask import Blueprint, request, jsonify, Response, session

from flask import flash
from flask_appbuilder import SimpleFormView
from flask_babel import lazy_gettext as _

# Importing base classes that we need to derive
from airflow.hooks.base import BaseHook
from airflow.www import auth, utils as wwwutils
from airflow.www.app import csrf
from airflow.security import permissions

from pprint import pprint
import random
import json

# Flask App Builder Things that I always use
from wtforms import Form, StringField
from wtforms.validators import DataRequired
from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from flask_appbuilder.forms import DynamicForm

# Importing base classes that we need to derive
from airflow.hooks.base import BaseHook
from airflow.models.baseoperator import BaseOperatorLink
from airflow.providers.amazon.aws.transfers.gcs_to_s3 import GCSToS3Operator

# Will show up in Connections screen in a future version
class PluginHook(BaseHook):
    pass

# Will show up under airflow.macros.test_plugin.plugin_macro
# and in templates through {{ macros.test_plugin.plugin_macro }}
def plugin_macro():
    pass

# Creating a flask blueprint to integrate the templates and static folder
bp = Blueprint(
    "{{cookiecutter.plugin_slug}}", __name__,
    template_folder='{{cookiecutter.plugin_slug}}/templates', # registers airflow/plugins/{{cookiecutter.plugin_slug}}/templates as a Jinja template folder
    static_folder='{{cookiecutter.plugin_slug}}/static', # registers airflow/plugins/{{cookiecutter.plugin_slug}}/static as a Jinja static folder
    static_url_path='{{cookiecutter.plugin_slug}}/static',# registers airflow/plugins/{{cookiecutter.plugin_slug}}/static as a Jinja template folder
    )

# Creating a flask appbuilder BaseView
class {{cookiecutter.plugin_class}}AppBuilderBaseView(AppBuilderBaseView):
    default_view = "test"

    @expose("/")
    def test(self):
        return self.render_template("{{cookiecutter.plugin_slug}}/test.html", content="Hello galaxy!")

# Creating a flask appbuilder BaseView
class {{cookiecutter.plugin_class}}AppBuilderBaseNoMenuView(AppBuilderBaseView):
    default_view = "test"

    @expose("/")
    def test(self):
        return self.render_template("{{cookiecutter.plugin_slug}}/test.html", content="Hello galaxy!")

v_appbuilder_view = {{cookiecutter.plugin_class}}AppBuilderBaseView()
v_appbuilder_package = {"name": "Test View",
                        "category": "Test Plugin",
                        "view": v_appbuilder_view}

v_appbuilder_nomenu_view = {{cookiecutter.plugin_class}}AppBuilderBaseNoMenuView()
v_appbuilder_nomenu_package = {
    "view": v_appbuilder_nomenu_view
}

# Creating flask appbuilder Menu Items
appbuilder_mitem = {
    "name": "Google",
    "href": "https://www.google.com",
    "category": "Search",
}
appbuilder_mitem_toplevel = {
    "name": "Apache",
    "href": "https://www.apache.org/",
}



# Defining the plugin class
class Airflow{{cookiecutter.plugin_class}}(AirflowPlugin):
    name = "{{cookiecutter.plugin_slug}}"
    hooks = [PluginHook]
    macros = [plugin_macro]
    flask_blueprints = [bp]
    appbuilder_views = [v_appbuilder_package, v_appbuilder_nomenu_package]
    appbuilder_menu_items = [appbuilder_mitem, appbuilder_mitem_toplevel]
    global_operator_extra_links = []
    operator_extra_links = []