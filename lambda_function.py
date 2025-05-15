import json
import logging
from products import ProductManager
from decimal import Decimal

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """AWS Lambda function to handle product creation requests."""
    logger.info(f"Received event: {json.dumps(event)}")
    
    try:
        # Initialize the product manager
        product_manager = ProductManager(endpoint_url=None)
        
        # Extract and validate body
        if not event:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'success': False,
                    'error': 'No event data provided'
                })
            }
            
        body = event.get('body', {})
        # Handle string body (from API Gateway)
        if isinstance(body, str):
            try:
                body = json.loads(body)
            except json.JSONDecodeError as e:
                return {
                    'statusCode': 400,
                    'body': json.dumps({
                        'success': False,
                        'error': f'Invalid JSON in request body: {str(e)}'
                    })
                }
        
        # Validate body is a dictionary
        if not isinstance(body, dict):
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'success': False,
                    'error': 'Request body must be a JSON object'
                })
            }
        
        # Extract required parameters
        required_params = ['name', 'description', 'base_price', 'category', 'color', 'size', 'inventory_count']
        missing_params = [param for param in required_params if param not in body]
        
        if missing_params:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'success': False,
                    'error': f'Missing required parameters: {", ".join(missing_params)}'
                })
            }
        
        # Convert float price to Decimal for DynamoDB compatibility
        try:
            base_price = Decimal(str(body['base_price']))
        except (ValueError, TypeError, decimal.InvalidOperation) as e:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'success': False,
                    'error': f'Invalid base_price value: {str(e)}'
                })
            }
        
        # Call the create_product method
        result = product_manager.create_product(
            name=body['name'],
            description=body['description'],
            base_price=base_price,  # Now using Decimal type
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