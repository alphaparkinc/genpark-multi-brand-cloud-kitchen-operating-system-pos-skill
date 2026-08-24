from client import MultiBrandCloudKitchenOperatingSystemPosClient

def main():
    client = MultiBrandCloudKitchenOperatingSystemPosClient()
    res = client.orchestrate_virtual_kitchen_station('DUBAI_MARINA_CLOUD_01', 8)
    print('Kitchen Hub: ' + res['kitchen_hub'] + ' | Dispatch Time: ' + str(res['average_cook_to_dispatch_mins']) + ' mins')
    print('Shared Ingredient Utilization: ' + str(res['raw_ingredient_shared_utilization_pct']) + '% | Safety Passed: ' + str(res['food_safety_hazard_analysis_passed']))
    print('Active Virtual Brands: ' + ', '.join(res['concurrent_virtual_brands_active']))

if __name__ == '__main__':
    main()
