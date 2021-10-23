<?php
/* Smarty version 3.1.39, created on 2021-10-23 10:35:28
  from '/Applications/MAMP/htdocs/prestashop/themes/classic/templates/index.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_6173c9507518b3_83946358',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'a1505df8612a556abd19783424e80d0648c81f95' => 
    array (
      0 => '/Applications/MAMP/htdocs/prestashop/themes/classic/templates/index.tpl',
      1 => 1634977225,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_6173c9507518b3_83946358 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, true);
?>


    <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_18639802736173c95074d636_32099010', 'page_content_container');
?>

<?php $_smarty_tpl->inheritance->endChild($_smarty_tpl, 'page.tpl');
}
/* {block 'page_content_top'} */
class Block_3924831716173c95074e048_69537593 extends Smarty_Internal_Block
{
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
}
}
/* {/block 'page_content_top'} */
/* {block 'hook_home'} */
class Block_6865607066173c95074f786_08709263 extends Smarty_Internal_Block
{
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

            <?php echo $_smarty_tpl->tpl_vars['HOOK_HOME']->value;?>

          <?php
}
}
/* {/block 'hook_home'} */
/* {block 'page_content'} */
class Block_21427487116173c95074ee89_16574220 extends Smarty_Internal_Block
{
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

          <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_6865607066173c95074f786_08709263', 'hook_home', $this->tplIndex);
?>

        <?php
}
}
/* {/block 'page_content'} */
/* {block 'page_content_container'} */
class Block_18639802736173c95074d636_32099010 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'page_content_container' => 
  array (
    0 => 'Block_18639802736173c95074d636_32099010',
  ),
  'page_content_top' => 
  array (
    0 => 'Block_3924831716173c95074e048_69537593',
  ),
  'page_content' => 
  array (
    0 => 'Block_21427487116173c95074ee89_16574220',
  ),
  'hook_home' => 
  array (
    0 => 'Block_6865607066173c95074f786_08709263',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

      <section id="content" class="page-home">
        <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_3924831716173c95074e048_69537593', 'page_content_top', $this->tplIndex);
?>


        <?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_21427487116173c95074ee89_16574220', 'page_content', $this->tplIndex);
?>

      </section>
    <?php
}
}
/* {/block 'page_content_container'} */
}
