import BackwardSearch
from BlocksWorld import BlocksWorld
from SpareTireDomain import SpareTireDomain
from DinnerDate import DinnerDate
from BackwardSearch import BackwardSearch
from ForwardSearch import ForwardSearch

if __name__ == '__main__':
    spareTire = SpareTireDomain()
    blocksWorld = BlocksWorld()
    dinnerDate = DinnerDate()


    forwardSearch = ForwardSearch(

        spareTire.get_initial(),
        spareTire.get_final(),
        spareTire.get_actions()

    )

    print("forward search result for spare tire domain: ")

    forwardSearch.search()

    print("===============")

    forwardSearch = ForwardSearch(

        blocksWorld.get_initial(),
        blocksWorld.get_final(),
        blocksWorld.get_actions()

    )

    print("forward search result for blocks world domain: ")

    forwardSearch.search()

    print("===============")

    forwardSearch = ForwardSearch(

        dinnerDate.get_initial(),
        dinnerDate.get_final(),
        dinnerDate.get_actions()

    )

    print("forward search result for dinner date domain: ")

    forwardSearch.search()

    print("===============")

    backwardSearch = BackwardSearch(

        spareTire.get_initial(),
        spareTire.get_final(),
        spareTire.get_actions()
    )

    print("backward search result for spare tire domain")

    backwardSearch.search()

    print("===============")

    # backwardSearch = BackwardSearch(
    #
    #     blocksWorld.get_initial(),
    #     blocksWorld.get_final(),
    #     blocksWorld.get_actions()
    # )
    #
    # print("backward search result for blocks world domain")
    #
    # backwardSearch.search()
    #
    # print("===============")
    #
    # backwardSearch = BackwardSearch(
    #
    #     dinnerDate.get_initial(),
    #     dinnerDate.get_final(),
    #     dinnerDate.get_actions()
    # )
    #
    # print("backward search result for dinner date domain")
    #
    # backwardSearch.search()
    #
    # print("===============")