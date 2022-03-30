# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class DashAgGridComponent(Component):
    """A DashAgGridComponent component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- animateRows (boolean; optional):
    animateRows for ag-Grid.

- columnDefs (list; optional):
    columnDefs for ag-Grid.

- columnState (list; optional):
    columnState for ag-Grid.

- debounceVerticalScrollbar (boolean; optional):
    debounceVerticalScrollbar for ag-Grid.

- enableCellChangeFlash (boolean; optional):
    enableCellChangeFlash for ag-Grid.

- enableCellTextSelection (boolean; optional):
    enableCellTextSelection for ag-Grid.

- gridApi (dict; optional):
    gridApi for ag-Grid.

- pagination (boolean; optional):
    pagination for ag-Grid.

- pinnedTopRowData (boolean | number | string | dict | list; optional):
    pinnedTopRowData for ag-Grid.

- resizedColumn (list; optional):
    resizedColumn for ag-Grid.

- rowBuffer (string; optional):
    rowBuffer for ag-Grid.

- rowData (list; optional):
    rowData for ag-Grid.

- rowDragEntireRow (boolean; optional):
    rowDragEntireRow for ag-Grid.

- rowDragManaged (boolean; optional):
    rowDragManaged for ag-Grid.

- rowSelection (string; optional):
    rowSelection for ag-grid.

- selectedRows (list; optional):
    selectedRows for ag-Grid.

- singleClickEdit (boolean; optional):
    singleClickEdit for ag-Grid.

- table_height (string; optional):
    table_height for ag-Grid.

- table_width (string; optional):
    table_width for ag-Grid.

- tooltipShowDelay (string; optional):
    tooltipShowDelay for ag-Grid."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, rowSelection=Component.UNDEFINED, gridApi=Component.UNDEFINED, columnDefs=Component.UNDEFINED, rowData=Component.UNDEFINED, selectedRows=Component.UNDEFINED, columnState=Component.UNDEFINED, resizedColumn=Component.UNDEFINED, table_height=Component.UNDEFINED, table_width=Component.UNDEFINED, pinnedTopRowData=Component.UNDEFINED, pagination=Component.UNDEFINED, animateRows=Component.UNDEFINED, enableCellChangeFlash=Component.UNDEFINED, rowDragManaged=Component.UNDEFINED, enableCellTextSelection=Component.UNDEFINED, rowDragEntireRow=Component.UNDEFINED, tooltipShowDelay=Component.UNDEFINED, singleClickEdit=Component.UNDEFINED, debounceVerticalScrollbar=Component.UNDEFINED, rowBuffer=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'animateRows', 'columnDefs', 'columnState', 'debounceVerticalScrollbar', 'enableCellChangeFlash', 'enableCellTextSelection', 'gridApi', 'pagination', 'pinnedTopRowData', 'resizedColumn', 'rowBuffer', 'rowData', 'rowDragEntireRow', 'rowDragManaged', 'rowSelection', 'selectedRows', 'singleClickEdit', 'table_height', 'table_width', 'tooltipShowDelay']
        self._type = 'DashAgGridComponent'
        self._namespace = 'dash_ag_grid_component'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'animateRows', 'columnDefs', 'columnState', 'debounceVerticalScrollbar', 'enableCellChangeFlash', 'enableCellTextSelection', 'gridApi', 'pagination', 'pinnedTopRowData', 'resizedColumn', 'rowBuffer', 'rowData', 'rowDragEntireRow', 'rowDragManaged', 'rowSelection', 'selectedRows', 'singleClickEdit', 'table_height', 'table_width', 'tooltipShowDelay']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(DashAgGridComponent, self).__init__(**args)
