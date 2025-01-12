import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-l10n-belgium",
    description="Meta package for oca-l10n-belgium Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-account_bank_statement_import_coda',
        'odoo11-addon-l10n_be_mis_reports',
        'odoo11-addon-l10n_be_vat_reports',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 11.0',
    ]
)
