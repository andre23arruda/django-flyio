JAZZMIN_SETTINGS = {
    'site_title': 'My API',
    'site_header': 'My API',
    'site_brand': 'My API',
    'site_logo': 'images/favicon.ico',
    'login_logo': 'images/logo.svg',
    'login_logo_dark': None,
    'site_logo_classes': 'img-circle',
    'site_icon': None,
    'welcome_sign': '',
    'copyright': 'copyright',
    'custom_css': 'css/custom-theme.css',

    'topmenu_links': [
        {'name': 'Home',  'url': 'admin:index', 'permissions': ['auth.view_user']},
    ],

    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',
    # 'show_ui_builder': True
}

JAZZMIN_UI_TWEAKS = {
    'navbar_small_text': False,
    'footer_small_text': False,
    'body_small_text': False,
    'brand_small_text': False,
    'brand_colour': False,
    'accent': 'accent-lightblue',
    'navbar': 'navbar-dark',
    'no_navbar_border': True,
    'navbar_fixed': True,
    'layout_boxed': False,
    'footer_fixed': False,
    'sidebar_fixed': True,
    'sidebar': 'sidebar-dark-primary',
    'sidebar_nav_small_text': False,
    'sidebar_disable_expand': False,
    'sidebar_nav_child_indent': False,
    'sidebar_nav_compact_style': False,
    'sidebar_nav_legacy_style': True,
    'sidebar_nav_flat_style': False,
    'theme': 'default',
    'dark_mode_theme': None,
    'button_classes': {
        'primary': 'btn-outline-primary',
        'secondary': 'btn-outline-secondary',
        'info': 'btn-outline-info',
        'warning': 'btn-outline-warning',
        'danger': 'btn-outline-danger',
        'success': 'btn-outline-success'
    }
}
