# TiVoRPC
Discord rich presence for TiVo made in Python3. Tested with a Virgin Media V6 TiVo Box.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Configuration
Edit config.json as follows:

| Key | Value |
| ------ | ------ |
| tivo_ip | Your TiVo Box IP |
| client_id | Your RPC Client ID (Check Important Notes) |
| large_image | RPC Art Asset Name To Use (Check Important Notes) |

## Usage

```bash
python TiVoRPC.py
```

## Important Notes
You __NEED__ to create an application [here](https://discord.com/developers/applications/) and grab your client ID, then create an "Art Asset" that will be displayed next to your status.

You __NEED__ to enable Network Remote Control in your TiVo settings. Google how to do this for your specific TiVo box.

Thanks to [David Newcomb](https://github.com/davidnewcomb) for his [JSON Virgin Media Channel Listings](http://www.bigsoft.co.uk/tools/virgin-media-channel-finder)
