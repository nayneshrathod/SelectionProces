class TwoDBRouteProductUser(object):
    # route_app_labels = {'ProductApp', 'UserApp', 'auth', 'contenttypes'}
    # route_app_labels = {'ProductApp', 'UserApp'}

    def db_for_read(self, model, **hints):
        "Point all operations on chinook models to 'productdb'"
        if model._meta.app_label == 'ProductApp':
            return 'productdb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on chinook models to 'productdb'"
        if model._meta.app_label == 'ProductApp':
            return 'productdb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in chinook app"
        if obj1._meta.app_label == 'ProductApp' and obj2._meta.app_label == 'ProductApp':
            return True
        # Allow if neither is chinook app
        elif 'ProductApp' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_syncdb(self, db, model):
        if db == 'productdb' or model._meta.app_label == "ProductApp":
            return False  # we're not using syncdb on our legacy database
        else:  # but all other models/databases are fine
            return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label == 'ProductApp':
            return db == 'productdb'
        return None


'''
    def db_for_read(self, model, **hints):
        """
        Attempts to read maternity, maternity_extended and paediatrics models go to medicalwale_sandbox_database.
        """
        if model._meta.app_label == 'ProductApp':
            return 'productdb'
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Attempts to write maternity, maternity_extended and paediatrics models go to medicalwale_sandbox_database.
        """
        if model._meta.app_label == 'ProductApp':
            return 'productdb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label == 'ProductApp':
            return db == 'productdb'
        return None


        def allow_syncdb(self, db, model):
            if db == 'productdb' or model._meta.app_label == "ProductApp":
                return False
            else:
                return True
    '''
