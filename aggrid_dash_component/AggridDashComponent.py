# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AggridDashComponent(Component):
    """An AggridDashComponent component.
AggridDashComponent is a component wrapped on ag-Grid.
It takes two property, `columnDefs`, and `rowData`
displays them.

Keyword arguments:

- id (string; optional)

- animateRows (boolean; optional)

- cellValueChanged (list; optional)

- columnDefs (list; optional)

- columnState (list; optional)

- debounceVerticalScrollbar (boolean; optional)

- enableCellChangeFlash (boolean; optional)

- gridApi (dict; optional)

- pagination (boolean; optional)

- pinnedTopRowData (boolean | number | string | dict | list; optional)

- resizedColumn (list; optional)

- rowBuffer (string; optional)

- rowData (list; optional)

- rowDragEntireRow (boolean; optional)

- rowDragManaged (boolean; optional)

- rowSelection (string; optional)

- selectedRows (list; optional)

- singleClickEdit (boolean; optional)

- table_height (string; optional)

- table_width (string; optional)

- tooltipShowDelay (string; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, rowSelection=Component.UNDEFINED, gridApi=Component.UNDEFINED, columnDefs=Component.UNDEFINED, rowData=Component.UNDEFINED, selectedRows=Component.UNDEFINED, columnState=Component.UNDEFINED, resizedColumn=Component.UNDEFINED, cellValueChanged=Component.UNDEFINED, table_height=Component.UNDEFINED, table_width=Component.UNDEFINED, pinnedTopRowData=Component.UNDEFINED, pagination=Component.UNDEFINED, animateRows=Component.UNDEFINED, enableCellChangeFlash=Component.UNDEFINED, rowDragManaged=Component.UNDEFINED, rowDragEntireRow=Component.UNDEFINED, tooltipShowDelay=Component.UNDEFINED, singleClickEdit=Component.UNDEFINED, debounceVerticalScrollbar=Component.UNDEFINED, rowBuffer=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animateRows', 'cellValueChanged', 'columnDefs', 'columnState', 'debounceVerticalScrollbar', 'enableCellChangeFlash', 'gridApi', 'pagination', 'pinnedTopRowData', 'resizedColumn', 'rowBuffer', 'rowData', 'rowDragEntireRow', 'rowDragManaged', 'rowSelection', 'selectedRows', 'singleClickEdit', 'table_height', 'table_width', 'tooltipShowDelay']
        self._type = 'AggridDashComponent'
        self._namespace = 'aggrid_dash_component'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animateRows', 'cellValueChanged', 'columnDefs', 'columnState', 'debounceVerticalScrollbar', 'enableCellChangeFlash', 'gridApi', 'pagination', 'pinnedTopRowData', 'resizedColumn', 'rowBuffer', 'rowData', 'rowDragEntireRow', 'rowDragManaged', 'rowSelection', 'selectedRows', 'singleClickEdit', 'table_height', 'table_width', 'tooltipShowDelay']
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
