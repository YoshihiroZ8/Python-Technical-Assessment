import json
import logging
from products import ProductManager

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """AWS Lambda function to handle product creation requests."""
    logger.info(f"Received event: {json.dumps(event)}")
    
    try:
        # Initialize the product manager
        product_manager = ProductManager()
        
        # Extract product data from the event
        body = event.get('body')
        if isinstance(body, str):
            body = json.loads(body)
        
        # Extract required parameters
        required_params = ['name', 'description', 'base_price', 'category', 'color', 'size', 'inventory_count']
        for param in required_params:
            if param not in body:
                return {
                    'statusCode': 400,
                    'body': json.dumps({
                        'success': False,
                        'error': f'Missing required parameter: {param}'
                    })
                }
        
        # Call the create_product method
        result = product_manager.create_product(
            name=body['name'],
            description=body['description'],
            base_price=float(body['base_price']),
            category=body['category'],
            color=body['color'],
            size=body['size'],
            inventory_count=int(body['inventory_count']),
            image_url=body.get('image_url'),
            tags=body.get('tags')
        )
        
        # Return the result
        if result['success']:
            return {
                'statusCode': 201,
                'body': json.dumps(result)
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps(result)
            }
            
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'success': False,
                'error': str(e)
            })
        }