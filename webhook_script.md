# Webhook Script

## Dependencies

Python 3: [Download link](https://www.python.org/downloads/)

Python `requests` module and `discord` module: To install, enter the following commands in cmd or a terminal:

```
pip install requests
```

```
pip install discord
```

## Usage

1. Run `check_artisan_stock_webhook.py` then close it to generate default settings file

2. Open `config.cfg` and add your discord webhook url for `url = `

3. Configure the message content you want to send when a mousepad goes from out of stock to in stock.

    `{Role Ping}` sends the content set for the pad under `[webhook_role_pings]`.

    `{Model}` sends the mousepad model.

    `{Hardness}` sends the mousepad hardness.

    `{Size}` sends the mousepad size.

    `{Color}` sends the mousepad color.

    `{Link}` sends a link to the mousepad's store page'

4. Optionally, edit `delay = ` in `config.cfg` to change the delay in seconds between checking stock. This delay is called twice so the real delay will be double the set delay.

5. Run `check_artisan_stock_webhook.py`

## Removing stock checks

### To entirely remove stock checks for a mousepad:

Remove it from `function_list` in `artisan_mousepads.py`.

For example, to remove all FX Shidenkai stock checks:

Take this:
```python
function_list = [cs_zero,fx_hayate,fx_hayate_otsu,fx_hayate_kou,fx_hien,fx_hien_ve,fx_zero,fx_raiden,fx_shidenkai]
```
and remove `fx_shidenkai`
```python
function_list = [cs_zero,fx_hayate,fx_hayate_otsu,fx_hayate_kou,fx_hien,fx_hien_ve,fx_zero,fx_raiden]
```

### To remove stock checks for specific hardnesses, sizes, or colors:

Remove them from their respective lists within the functions in `artisan_mousepads.py`. Check the dictionaries to find what each number checks for.

For example, to remove the XSoft check from the FX Shidenkai:

Take this:
```python
def fx_shidenkai():
    models = ["18"]
    hardnesses = ["0","2"]
    sizes = ["1","2","3","4"]
    colors = ["3","6","7"]
    return [models,hardnesses,sizes,colors]
```
and edit the `hardnesses` list:
```python
def fx_shidenkai():
    models = ["18"]
    hardnesses = ["2"]
    sizes = ["1","2","3","4"]
    colors = ["3","6","7"]
    return [models,hardnesses,sizes,colors]
```

## Adding stock checks

### Adding an entirely new pad

1. Find the model, hardnesses, sizes, and colors using your browser's developer/debug tools on the network tab. The data will be in the requests tab for `get_syouhin.php`. 

    The model will be the first one or two numbers after `sir`.

    The hardness will be the last number in `sir`.

    The size will be the number in `size`.

    The color will be the number after `color`.

2. Add the model and link to the dictionary in `artisan_mousepads.py` along with hardnesses, sizes, and colors if those are not already accounted for. For example, adding a new mousepad model named `new_pad`:
    ```python
    dict_mousepad_models = {
        "1" : "CS Zero",
        "11" : "FX Hayate",
        "12" : "FX Hayate Otsu",
        "13" : "FX Hayate Kou",
        "14" : "FX Hien",
        "15" : "FX Hien VE",
        "16" : "FX Zero",
        "17" : "FX Raiden",
        "18" : "FX Shidenkai",
        "19" : "New Pad"
    }
    ```
3. Make a new function for this new stock check in `artisan_mousepads.py`. For example, adding a function named `new_pad`:
    ```python
    def new_pad():
        models = ["19"]
        hardnesses = ["0","2"]
        sizes = ["1","2","3","4"]
        colors = ["3","6","7"]
        return [models,hardnesses,sizes,colors]
    ```
4. Add this function to the functions list in `artisan_mousepads.py`. For example, adding the `new_pad` function to the list: 
    ```python
    function_list = [new_pad,cs_zero,fx_hayate,fx_hayate_otsu,fx_hayate_kou,fx_hien,fx_hien_ve,fx_zero,fx_raiden,fx_shidenkai]
    ```

### Adding new options to an existing pad

1. Find the new hardnesses, sizes, or colors using your browser's developer/debug tools on the network tab. The data will be in the requests tab for `get_syouhin.php`. 

    The hardness will be the last number in `sir`.

    The size will be the number in `size`.

    The color will be the number after `color`.

2. Add the hardnesses, sizes, and colors to the dictionary if those are not already accounted for in `artisan_mousepads.py`. For example, adding color `9` as `New Color`:

    ```python
    dict_colors = {
    "1" : "Red",
    "2" : "Blue",
    "3" : "Black",
    "5" : "Black",
    "6" : "White",
    "7" : "Pink",
    "8" : "Brown",
    "9" : "New Color"
    }
    ```

3. Add the new hardnesses, sizes, or colors to the function in `artisan_mousepads.py`. For example, adding color `9` to the FX Raiden:

    ```python
    def fx_raiden():
    models = ["17"]
    hardnesses = ["0","2"]
    sizes = ["2","3","4"]
    colors = ["8","9"]
    return [models,hardnesses,sizes,colors]
    ```