import discord
from discord.ext import commands

# Configuración inicial del bot
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='*', intents=intents)

# IDs de tu servidor y roles
GUILD_ID = 763879230173872128  # Reemplaza con el ID de tu servidor
ROLE_EMOJI_MAP = {
    "<:DanyMyers:1129921010376913077>": 1129923870468608074,  # Reemplaza con el ID del primer rol
    "<:TruenoCoyote:1277729893173559447>": 1129923627161231443,  # Reemplaza con el ID del segundo rol
    "<:DUBQW:1129922654070112358>": 1129924063708590214,  # Reemplaza con el ID del tercer rol
    "<:WOTota:1277730062237700187>": 1197028210127413328,  #WoToTa Reemplaza con el ID del cuarto rol
}

@bot.event
async def on_ready():
    print(f'{bot.user} ha iniciado sesión y está listo.')

@bot.command()
async def enviar_mensaje(ctx):
    # Reemplaza "ID_DEL_CANAL" con el ID del canal
    canal = bot.get_channel(1130155153933205504)
    
    if canal:
         message = await ctx.send("Comunidades:\n <:DanyMyers:1129921010376913077>: DanyMyers:\n <:DUBQW:1129922654070112358>:DURBQW1\n <:TruenoCoyote:1277729893173559447>: TruenoCoyote:\n <:WOTota:1277730062237700187>: WOTota")
    for emoji in ROLE_EMOJI_MAP.keys():
        await message.add_reaction(emoji)
    else:
        await ctx.send("No se pudo encontrar el canal.")

@bot.event
async def on_member_join(member):
    try:
        # Reemplaza 'CANAL_ID' con la ID real del canal de roles
        canal_roles_id = 1130155153933205504  # Reemplaza con la ID del canal de roles
        
        # Enviar un mensaje directo (DM) al nuevo miembro
        await member.send(
            f"¡Bienvenido/a a {member.guild.name}! 🎉\n\n"
            f"Para obtener un rol en nuestro servidor, por favor visita el canal <#{canal_roles_id}> y reacciona al mensaje correspondiente."
        )
        
        print(f"Se envió un mensaje de bienvenida a {member.name}.")
    except discord.Forbidden:
        # Manejar el caso en que el bot no puede enviar un DM al usuario
        print(f"No se pudo enviar un mensaje directo a {member.name}.")
        # Opcional: Puedes enviar un mensaje en un canal de bienvenida público si falla el DM


@bot.event
async def on_raw_reaction_add(payload):
    if payload.guild_id != GUILD_ID:
        return
    
    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return

    role_id = ROLE_EMOJI_MAP.get(payload.emoji.name)
    if role_id is None:
        return

    role = guild.get_role(role_id)
    if role is None:
        return

    member = guild.get_member(payload.user_id)
    if member is None:
        return

    try:
        await member.add_roles(role)
        print(f"Se ha añadido el rol {role.name} a {member.display_name}")
    except Exception as e:
        print(f"No se pudo añadir el rol: {e}")

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.guild_id != GUILD_ID:
        return
    
    guild = bot.get_guild(payload.guild_id)
    if guild is None:
        return

    role_id = ROLE_EMOJI_MAP.get(payload.emoji.name)
    if role_id is None:
        return

    role = guild.get_role(role_id)
    if role is None:
        return

    member = guild.get_member(payload.user_id)
    if member is None:
        return

    try:
        await member.remove_roles(role)
        print(f"Se ha eliminado el rol {role.name} de {member.display_name}")
    except Exception as e:
        print(f"No se pudo eliminar el rol: {e}")

# Iniciar el bot
bot.run('MTI4MjA0NDYwNTM1NzEwMTIxNA.GCUHIU.oR5SEGWT2tAmga3uEGZngDlbdeURkPkjTxAPGs')
