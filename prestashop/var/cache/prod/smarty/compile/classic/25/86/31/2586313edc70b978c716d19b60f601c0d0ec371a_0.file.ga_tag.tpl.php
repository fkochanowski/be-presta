<?php
/* Smarty version 3.1.39, created on 2022-01-06 18:16:39
  from '/home/projek28/domains/projekt-pg.vxm.pl/public_html/prestashop/modules/ps_googleanalytics/views/templates/hook/ga_tag.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_61d723f740ce99_20037357',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '2586313edc70b978c716d19b60f601c0d0ec371a' => 
    array (
      0 => '/home/projek28/domains/projekt-pg.vxm.pl/public_html/prestashop/modules/ps_googleanalytics/views/templates/hook/ga_tag.tpl',
      1 => 1636234537,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_61d723f740ce99_20037357 (Smarty_Internal_Template $_smarty_tpl) {
if ((!empty($_smarty_tpl->tpl_vars['jsCode']->value))) {?>
    
    <?php echo '<script'; ?>
 type="text/javascript">
        document.addEventListener('DOMContentLoaded', function() {
            var MBG = GoogleAnalyticEnhancedECommerce;
            MBG.setCurrency('<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['isoCode']->value,'htmlall','UTF-8' ));?>
');
            <?php echo $_smarty_tpl->tpl_vars['jsCode']->value;?>

        });
    <?php echo '</script'; ?>
>
    
<?php }
}
}
