import pytest
import pandas as pd

def merge(X):

    '''
    merge function has been used to merge the sub-columns into single column
    It operates on per row basis
    '''
    a = ''
    for col in X:
        a = a + str(col)
    return a

def growth_calc(X):

    '''
    growth_calc function has been used to calculate the growth of funding between the years 2008 and 2009
    It operates on per row basis
    '''
    if X['C1) Funding FY2008'] >0:
        return ((X['C2) Funding FY2009'] - X['C1) Funding FY2008'])/X['C1) Funding FY2008'])*100
    return 1

def target(X):

    '''
    target function has been used to produce target or dependent variable for training of model
    It operates on per row basis
    '''

    if X['% Growth']> 0:
        return 1
    else:
        return 0


def test_merge():
    '''
    Test function for merge
    '''
    assert merge([1,2,3,4,5]) == '12345'

def test_growth():
    '''
    Test function for growth_calc
    '''
    df = pd.DataFrame(data=[[20,30],[40,20]], columns=['C1) Funding FY2008', 'C2) Funding FY2009'])
    assert growth_calc(df.loc[0]) == 50
    assert growth_calc(df.loc[1]) == -50

def test_target():
    '''
    Test function for target
    '''
    df  = pd.DataFrame([[-3],[3]], columns=['% Growth'])
    assert target(df.loc[0]) == 0
    assert target(df.loc[1]) == 1
