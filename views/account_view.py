<record id="view_account_account_form_inherited" model="ir.ui.view">
    <field name="name">account.account.form.inherited</field>
    <field name="model">account.account</field>
    <field name="inherit_id" ref="account.view_account_form"/>
    <field name="arch" type="xml">
        <xpath expr="//page[@name='general']" position="inside">
            <field name="move_lines">
                <tree>
                    <field name="name"/>
                </tree>
            </field>
        </xpath>
    </field>
</record>