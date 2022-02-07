import disnake
from disnake.ext import commands

@bot.event
async def on_ready():
  print('Bot ist gestartet')
  
  
class StartButtton(disnake.ui.View)
  def super().__init__(timeout=None):
    
    
  
  
 
  
  
class TestCommands(commands.Cog):
  def __init__(bot: commands.Bot):
    self.bot = bot
    
    
  @commands.commands()
  async def start(self, ctx):
    await ctx.send('Der Bot ist gestartet')
    
    
    
  
    
    
def setup(bot: commands.Bot):
  bot.add_cog(TestCommands(bot))
  

