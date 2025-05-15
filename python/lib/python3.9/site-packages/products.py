import boto3
import uuid
from datetime import datetime
import json

class ProductManager:
    def __init__(self, table_name='products', region='us-east-1'):
        """Initialize the ProductManager with the DynamoDB table name."""
        self.dynamodb = boto3.resource('dynamodb', region_name=region)
        self.table = self.dynamodb.Table(table_name)
    
    def create_product(self, name, description, base_price, category, color, size, 
                      inventory_count, image_url=None, tags=None):
        """Create a new product with variant in the DynamoDB table."""
        try:
            # Generate unique IDs
            product_id = str(uuid.uuid4())
            variant_id = f"{color}-{size}"
            
            # Calculate final price (could include logic based on size)
            price = base_price
            if size in ['XL', 'XXL']:
                price += 2.00  # Price adjustment for larger sizes
            
            # Current timestamp
            timestamp = datetime.now().isoformat()
            
            # Create item with all attributes
            item = {
                'product_id': product_id,
                'variant_id': variant_id,
                'name': name,
                'description': description,
                'base_price': base_price,
                'color': color,
                'size': size,
                'price': price,
                'category': category,
                'inventory_count': inventory_count,
                'created_at': timestamp,
                'updated_at': timestamp
            }
            
            # Add optional attributes if provided
            if image_url:
                item['image_url'] = image_url
            
            if tags:
                item['tags'] = json.dumps(tags)
            
            # Put item in DynamoDB table
            response = self.table.put_item(Item=item)
            
            return {
                'success': True,
                'product_id': product_id,
                'variant_id': variant_id,
                'message': 'Product created successfully'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def get_product(self, product_id, variant_id):
        """Retrieve a specific product variant from the DynamoDB table."""
        try:
            response = self.table.get_item(
                Key={
                    'product_id': product_id,
                    'variant_id': variant_id
                }
            )
            
            if 'Item' in response:
                return {
                    'success': True,
                    'product': response['Item']
                }
            else:
                return {
                    'success': False,
                    'message': 'Product not found'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def list_products(self, limit=100):
        """List all products in the DynamoDB table."""
        try:
            response = self.table.scan(Limit=limit)
            
            return {
                'success': True,
                'products': response.get('Items', []),
                'count': len(response.get('Items', []))
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def update_product(self, product_id, variant_id, updates):
        """Update a specific product variant in the DynamoDB table."""
        try:
            # Prepare update expression and attribute values
            update_expression = "SET updated_at = :timestamp"
            expression_attribute_values = {
                ':timestamp': datetime.now().isoformat()
            }
            
            # Add each update to the expression
            for key, value in updates.items():
                if key not in ['product_id', 'variant_id']:  # Don't update keys
                    update_expression += f", {key} = :{key}"
                    expression_attribute_values[f":{key}"] = value
            
            # Update the item in DynamoDB
            response = self.table.update_item(
                Key={
                    'product_id': product_id,
                    'variant_id': variant_id
                },
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
                ReturnValues="UPDATED_NEW"
            )
            
            return {
                'success': True,
                'updated_attributes': response.get('Attributes', {}),
                'message': 'Product updated successfully'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def delete_product(self, product_id, variant_id):
        """Delete a specific product variant from the DynamoDB table."""
        try:
            response = self.table.delete_item(
                Key={
                    'product_id': product_id,
                    'variant_id': variant_id
                },
                ReturnValues="ALL_OLD"
            )
            
            if 'Attributes' in response:
                return {
                    'success': True,
                    'deleted_product': response['Attributes'],
                    'message': 'Product deleted successfully'
                }
            else:
                return {
                    'success': True,
                    'message': 'Product may not have existed'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

# Example usage
if __name__ == "__main__":
    # Initialize the product manager
    product_manager = ProductManager()
    
    # Create a new product
    result = product_manager.create_product(
        name="Graphic T-Shirt: Mountain Design",
        description="A beautiful t-shirt with mountain scenery",
        base_price=19.99,
        category="T-Shirts",
        color="Blue",
        size="M",
        inventory_count=100,
        image_url="https://example.com/images/mountain-tshirt-blue-m.jpg",
        tags=["mountains", "nature", "outdoor"]
    )
    
    print("Create result:", result)