//
//  IngredientsRequest.h
//  Drinks-Query
//
//  Created by Des Marks on 7/30/16.
//  Copyright © 2016 Des Marks. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface IngredientsRequest : NSObject
-(NSString *) getIngredientWithQueryParams:(NSMutableArray *)queryItems;
@end