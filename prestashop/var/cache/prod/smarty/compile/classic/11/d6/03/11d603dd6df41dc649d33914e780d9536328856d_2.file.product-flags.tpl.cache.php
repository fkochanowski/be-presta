<?php
/* Smarty version 3.1.39, created on 2022-01-06 17:47:55
  from '/home/projek28/domains/projekt-pg.vxm.pl/public_html/prestashop/themes/classic/templates/catalog/_partials/product-flags.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_61d71d3b1ef138_27781027',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '11d603dd6df41dc649d33914e780d9536328856d' => 
    array (
      0 => '/home/projek28/domains/projekt-pg.vxm.pl/public_html/prestashop/themes/classic/templates/catalog/_partials/product-flags.tpl',
      1 => 1636154622,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_61d71d3b1ef138_27781027 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, false);
$_smarty_tpl->compiled->nocache_hash = '59424060361d71d3b1ecf01_43267122';
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_70130203061d71d3b1edb60_93522599', 'product_flags');
?>

<?php }
/* {block 'product_flags'} */
class Block_70130203061d71d3b1edb60_93522599 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'product_flags' => 
  array (
    0 => 'Block_70130203061d71d3b1edb60_93522599',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

    <ul class="product-flags js-product-flags">
        <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['product']->value['flags'], 'flag');
$_smarty_tpl->tpl_vars['flag']->do_else = true;
if ($_from !== null) foreach ($_from as $_smarty_tpl->tpl_vars['flag']->value) {
$_smarty_tpl->tpl_vars['flag']->do_else = false;
?>
            <li class="product-flag <?php echo htmlspecialchars($_smarty_tpl->tpl_vars['flag']->value['type'], ENT_QUOTES, 'UTF-8');?>
"><?php echo htmlspecialchars($_smarty_tpl->tpl_vars['flag']->value['label'], ENT_QUOTES, 'UTF-8');?>
</li>
        <?php
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
    </ul>
<?php
}
}
/* {/block 'product_flags'} */
}
