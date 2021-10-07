# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AggridDashComponent(Component):
    """An AggridDashComponent component.
AggridDashComponent is a component wrapped on ag-Grid.
It takes two property, `columnDefs`, and `rowData`
displays them.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- columnDefs (list; optional):
    columnDefs for ag-Grid.

- gridApi (dict; optional):
    gridApi for ag-Grid.

- rowData (list; optional):
    rowData for ag-Grid.

- selectedRows (list; optional):
    selectedRows for ag-Grid.

- table_height (string; optional)

- table_width (string; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, gridApi=Component.UNDEFINED, columnDefs=Component.UNDEFINED, rowData=Component.UNDEFINED, selectedRows=Component.UNDEFINED, table_height=Component.UNDEFINED, table_width=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'columnDefs', 'gridApi', 'rowData', 'selectedRows', 'table_height', 'table_width']
        self._type = 'AggridDashComponent'
        self._namespace = 'aggrid_dash_component'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'columnDefs', 'gridApi', 'rowData', 'selectedRows', 'table_height', 'table_width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AggridDashComponent, self).__init__(**args)
