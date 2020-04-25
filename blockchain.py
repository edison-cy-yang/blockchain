class Blockchain(object):
  def __init__(self):
    self.chain = []
    self.current_transactions = []

  def new_block(self):
    #creates a new block and adds it to the chain
    pass

  def new_transaction(self):
    """
    creates a new transaction to go into the next minded Block
    :param sender: <str> Address of the sender
    :param recipient: <Str> address of the recipient
    :param amount: <int> amount
    :return: <int> the index of the block that will hold this transaction
    """
    pass

  @staticmethod
  def hash(block):
    #hashes a block
    pass

  @property
  def last_block(self);
    #returns the last block in the chain
    pass