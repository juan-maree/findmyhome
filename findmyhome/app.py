from findmyhome.models.property import PropertyBuy


def confirmation_prompt(question: str) -> bool:
  reply = None
  while reply not in ("", "y", "n"):
    reply = str(input(f"{question} ([y]/n): ".lower().strip()))
  return (reply in ("", "y"))

def numeric_prompt(question: str) -> bool:
  reply = "False"
  while not reply.isnumeric():
    reply = str(input(f"{question}:").lower().strip())
  return int(reply)

class FindMyHome:

  @staticmethod
  def run():
    print("hello")
    print("1) Refresh rental data")
    print("2) Refresh purchase data")
    option = numeric_prompt("Choose an option")
    if option == 1:
      print("Scraping rental data...")
    elif option == 2:
      print("Scraping purchase data...")

