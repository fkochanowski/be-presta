<?php
/* Smarty version 3.1.39, created on 2021-10-23 10:36:12
  from '/Applications/MAMP/htdocs/prestashop/admin06419c15h/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_6173c97cbbf7b0_66961886',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '46199a1d0bcc346a77b17ef40886bafa05e45da7' => 
    array (
      0 => '/Applications/MAMP/htdocs/prestashop/admin06419c15h/themes/default/template/content.tpl',
      1 => 1634977227,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6173c97cbbf7b0_66961886 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="ajax_confirmation" class="alert alert-success hide"></div>
<div id="ajaxBox" style="display:none"></div>

<div class="row">
	<div class="col-lg-12">
		<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
			<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

		<?php }?>
	</div>
</div>
<?php }
}
