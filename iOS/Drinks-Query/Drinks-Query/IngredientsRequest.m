//
//  IngredientsRequest.m
//  Drinks-Query
//
//  Created by Des Marks on 7/30/16.
//  Copyright © 2016 Des Marks. All rights reserved.
//

#import "IngredientsRequest.h"

@interface IngredientsRequest ()
@end

@implementation IngredientsRequest

-(NSString *) getIngredientWithQueryParams:(NSMutableArray *)queryItems
{
    NSMutableURLRequest *request = [self createIngredientRequestWithQueryItems:queryItems];
    
    NSData *responseData = [self sendIngredientRequest:request];
    
    return [[NSString alloc] initWithData:responseData encoding:NSUTF8StringEncoding];
}

- (NSMutableURLRequest *) createIngredientRequestWithQueryItems:(NSMutableArray *)queryItems
{
    NSURLComponents *pathComponents = [[NSURLComponents alloc] init];
    
    pathComponents.scheme = @"https";
    pathComponents.host = @"127.0.0.1";
    pathComponents.path = @"/api/";
    pathComponents.port = [[NSNumber alloc] initWithInt:5000];
    
    //Add table to the path
    pathComponents.path = [pathComponents.path stringByAppendingString:[queryItems objectAtIndex:0]];
    //Add table query
    pathComponents.path = [pathComponents.path stringByAppendingString:[queryItems objectAtIndex:1]];
    
    NSURL *url = pathComponents.URL;
    
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] initWithURL:url];

     [request setHTTPMethod:@"GET"];
    
    return request;
}

- (NSData *) sendIngredientRequest:(NSMutableURLRequest *)request
{
    NSHTTPURLResponse *response = nil;
    NSError *requestError = nil;
    
    NSData *responseData = [NSURLConnection sendSynchronousRequest:request returningResponse:&response error:&requestError];
    
    return responseData;
}


@end
